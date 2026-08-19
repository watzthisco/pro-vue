#!/usr/bin/env python3
"""Remove slide parts that are no longer referenced from the slide list.

python-pptx unlinks a deleted slide from the presentation but leaves its XML
in the package, so the removed content is still in the file. This rewrites the
archive with those parts (and their notes slides and rels) dropped.
"""
import posixpath, shutil, sys, zipfile

from lxml import etree

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
CT = '{http://schemas.openxmlformats.org/package/2006/content-types}'


def live_slides(z):
    pres = etree.fromstring(z.read('ppt/presentation.xml'))
    rels = {rel.get('Id'): rel.get('Target')
            for rel in etree.fromstring(z.read('ppt/_rels/presentation.xml.rels'))}
    live = set()
    for sldId in pres.iter(f'{P}sldId'):
        target = rels[sldId.get(f'{R}id')]
        live.add(posixpath.normpath(posixpath.join('ppt', target)))
    return live


def prune(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    live = live_slides(z)

    all_slides = {n for n in names if n.startswith('ppt/slides/slide')
                  and n.endswith('.xml')}
    dead = all_slides - live
    if not dead:
        print('nothing to prune')
        return 0

    drop = set(dead)
    for n in dead:
        rels = f'ppt/slides/_rels/{posixpath.basename(n)}.rels'
        if rels in names:
            drop.add(rels)
            # A dead slide's notes slide goes with it.
            for rel in etree.fromstring(z.read(rels)):
                if rel.get('Type', '').endswith('/notesSlide'):
                    notes = posixpath.normpath(
                        posixpath.join('ppt/slides', rel.get('Target')))
                    drop.add(notes)
                    notes_rels = (f'{posixpath.dirname(notes)}/_rels/'
                                  f'{posixpath.basename(notes)}.rels')
                    if notes_rels in names:
                        drop.add(notes_rels)

    # Rebuild [Content_Types].xml without the dropped overrides.
    ct = etree.fromstring(z.read('[Content_Types].xml'))
    for override in list(ct):
        part = (override.get('PartName') or '').lstrip('/')
        if part in drop:
            ct.remove(override)
    new_ct = etree.tostring(ct, xml_declaration=True, encoding='UTF-8',
                            standalone=True)

    # Other parts (viewProps, for instance) may still point at the dropped
    # slides. Strip those relationship entries too.
    rewritten_rels = {}
    stripped = 0
    for n in names:
        if not n.endswith('.rels') or n in drop:
            continue
        root = etree.fromstring(z.read(n))
        base = posixpath.dirname(posixpath.dirname(n))
        removed = False
        for rel in list(root):
            if rel.get('TargetMode') == 'External':
                continue
            target = posixpath.normpath(posixpath.join(base, rel.get('Target')))
            if target in drop:
                root.remove(rel)
                removed = True
                stripped += 1
        if removed:
            rewritten_rels[n] = etree.tostring(
                root, xml_declaration=True, encoding='UTF-8', standalone=True)
    if stripped:
        print(f'stripped {stripped} relationships pointing at dropped parts')

    # ppt/viewProps.xml keeps an outline-view list of slides by r:id. Drop the
    # entries whose relationship has just been removed.
    vp_name = 'ppt/viewProps.xml'
    if vp_name in names:
        vp = etree.fromstring(z.read(vp_name))
        kept_rids = {rel.get('Id') for rel in
                     etree.fromstring(z.read('ppt/_rels/viewProps.xml.rels'))} \
            if 'ppt/_rels/viewProps.xml.rels' in names else set()
        kept_rids -= {rid for rid, (t, m) in []}
        # Recompute from the rewritten rels if we changed them.
        if 'ppt/_rels/viewProps.xml.rels' in rewritten_rels:
            kept_rids = {rel.get('Id') for rel in
                         etree.fromstring(rewritten_rels['ppt/_rels/viewProps.xml.rels'])}
        removed_sld = 0
        for el in list(vp.iter(f'{P}sld')):
            if el.get(f'{R}id') not in kept_rids:
                el.getparent().remove(el)
                removed_sld += 1
        if removed_sld:
            rewritten_rels[vp_name] = etree.tostring(
                vp, xml_declaration=True, encoding='UTF-8', standalone=True)
            print(f'removed {removed_sld} stale outline-view entries from viewProps')

    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as out:
        for item in z.infolist():
            if item.filename in drop:
                continue
            if item.filename == '[Content_Types].xml':
                data = new_ct
            elif item.filename in rewritten_rels:
                data = rewritten_rels[item.filename]
            else:
                data = z.read(item.filename)
            out.writestr(item, data)
    z.close()
    shutil.move(tmp, path)
    print(f'pruned {len(drop)} orphaned parts ({len(dead)} slides)')
    return len(drop)


if __name__ == '__main__':
    prune(sys.argv[1])

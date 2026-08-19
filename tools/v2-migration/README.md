# Version 2.0 migration tooling

One-shot scripts used to produce the Version 2.0 courseware from Version 1.5.
They are kept because they hold the full text of the new slides and lab steps,
which makes the next revision an edit rather than a rewrite.

| File                  | Purpose                                                        |
| --------------------- | -------------------------------------------------------------- |
| `scaffold.py`         | Writes package.json, vite.config.js, eslint.config.js and index.html for every Vue project |
| `apply.py`            | Copies the migrated `src/` and `tests/` files into each lab and solution |
| `verify.sh`           | Installs, builds, tests and lints every project                |
| `docxlib.py`          | Paragraph-range surgery helpers for python-docx                |
| `labcontent.py`       | The new lab-manual text, by section                            |
| `build_labmanual.py`  | Builds `Professional-Vue-v2.0.docx` from the v1.5 manual        |
| `build_setup.py`      | Builds the Version 2.0 `Setup-Instructions.docx`               |
| `build_coursedesc.py` | Refreshes the Version 2.0 course description                   |
| `pptxlib.py`          | Slide rewrite/insert/delete helpers for python-pptx            |
| `slidecontent.py`     | The new slide text, keyed by v1.5 slide number                 |
| `build_deck.py`       | Builds `Professional-Vue-v2.0.pptx` from the v1.5 deck          |
| `prune_pptx.py`       | Drops deleted slides' parts from the package instead of just unlinking them |

## Requirements

```
pip install python-docx python-pptx openpyxl lxml
```

## Rebuilding the Version 2.0 documents

Each build script reads from `presentation/Version 1.5/` and writes to
`presentation/Version 2.0/`, so they are safe to re-run after editing the
content modules:

```
python3 tools/v2-migration/build_labmanual.py
python3 tools/v2-migration/build_setup.py
python3 tools/v2-migration/build_deck.py
python3 tools/v2-migration/prune_pptx.py "presentation/Version 2.0/Professional-Vue-v2.0.pptx"
```

`build_coursedesc.py` edits `presentation/Version 2.0/Vue-CourseDescription.docx`
in place and is not idempotent — restore that file from git before re-running it.

Note that the scripts hard-code `/home/user/pro-vue` as the repository root;
change `ROOT` at the top of each one if you check the repo out elsewhere.

## Regenerating the lab and solution projects

```
python3 tools/v2-migration/scaffold.py
python3 tools/v2-migration/apply.py
bash    tools/v2-migration/verify.sh
```

`apply.py` reads its sources from `.migration/src/`, which is not checked in —
the migrated files now live in the lab and solution directories themselves, so
these two scripts are of historical interest only.

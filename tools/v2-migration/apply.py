#!/usr/bin/env python3
"""Copy the migrated Vue 3 sources into each lab/solution project."""
import os, shutil, sys

ROOT = "/home/user/pro-vue"
SRC = os.path.join(ROOT, ".migration/src")

# Per-project mapping: destination path (relative to project) -> source file in .migration/src
MAP = {
    "solutions/lab03": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab03.vue",
        "src/components/Header.vue": "components/Header.lab03.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
    },
    "solutions/lab04": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab04.vue",
        "src/components/Header.vue": "components/Header.lab03.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab04.vue",
        "src/components/Footer.vue": "components/Footer.lab04.vue",
    },
    "solutions/lab05": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab04.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab05.vue",
        "src/components/Footer.vue": "components/Footer.lab04.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.spec.js",
    },
    "solutions/lab11": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab04.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab11.vue",
        "src/components/Footer.vue": "components/Footer.lab04.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab11.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab11.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab12": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab12.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab11.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab12.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab13": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab12.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab11.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab13.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab14": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab12.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab11.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab14.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab15": {
        "src/main.js": "main.lab03.js",
        "src/App.vue": "App.lab12.vue",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab15.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab16": {
        "src/main.js": "main.lab16.js",
        "src/App.vue": "App.lab12.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab16.js",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab16.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab17": {
        "src/main.js": "main.lab16.js",
        "src/App.vue": "App.lab12.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab16.js",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab17.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab18": {
        "src/main.js": "main.lab18.js",
        "src/App.vue": "App.lab12.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab16.js",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab18.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab17.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "src/components/Tag.vue": "components/Tag.vue",
        "src/components/TagList.vue": "components/TagList.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab19": {
        "src/main.js": "main.lab16.js",
        "src/App.vue": "App.lab12.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab16.js",
        "src/composables/useArticleFilter.js": "composables/useArticleFilter.js",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab19.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab20": {
        "src/main.js": "main.lab20.js",
        "src/App.vue": "App.lab12.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab20.js",
        "src/composables/useArticleFilter.js": "composables/useArticleFilter.js",
        "src/stores/home.js": "stores/home.js",
        "src/components/Header.vue": "components/Header.lab05.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab12.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab20.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.spec.js",
        "tests/components/Home.spec.js": "tests/Home.shallow.spec.js",
    },
    "solutions/lab21": {
        "src/main.js": "main.lab21.js",
        "src/App.vue": "App.lab21.vue",
        "src/common/config.js": "common/config.js",
        "src/common/api.service.js": "common/api.service.lab20.js",
        "src/composables/useArticleFilter.js": "composables/useArticleFilter.js",
        "src/stores/home.js": "stores/home.js",
        "src/router/index.js": "router/index.lab21.js",
        "src/components/Header.vue": "components/Header.lab21.vue",
        "src/components/HelloWorld.vue": "components/HelloWorld.vue",
        "src/components/Home.vue": "components/Home.lab12.vue",
        "src/components/Footer.vue": "components/Footer.lab21.vue",
        "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
        "src/components/ArticleList.vue": "components/ArticleList.lab20.vue",
        "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
        "src/components/Login.vue": "components/Login.lab21.vue",
        "tests/example.spec.js": "tests/example.spec.js",
        "tests/components/Footer.spec.js": "tests/Footer.spec.js",
        "tests/components/Header.spec.js": "tests/Header.router.spec.js",
        "tests/components/Home.spec.js": "tests/Home.store.spec.js",
    },
}

# lab22, lab23 and lab24 share the same tree.
_LAB22 = {
    "src/main.js": "main.lab21.js",
    "src/App.vue": "App.lab21.vue",
    "src/common/config.js": "common/config.js",
    "src/common/api.service.js": "common/api.service.lab22.js",
    "src/common/jwt.service.js": "common/jwt.service.js",
    "src/composables/useArticleFilter.js": "composables/useArticleFilter.js",
    "src/stores/home.js": "stores/home.js",
    "src/stores/auth.js": "stores/auth.js",
    "src/router/index.js": "router/index.lab22.js",
    "src/components/Header.vue": "components/Header.lab22.vue",
    "src/components/HelloWorld.vue": "components/HelloWorld.vue",
    "src/components/Home.vue": "components/Home.lab22.vue",
    "src/components/Footer.vue": "components/Footer.lab21.vue",
    "src/components/GlobalFeed.vue": "components/GlobalFeed.vue",
    "src/components/ArticleList.vue": "components/ArticleList.lab20.vue",
    "src/components/ArticlePreview.vue": "components/ArticlePreview.lab15.vue",
    "src/components/Login.vue": "components/Login.lab22.vue",
    "src/components/Register.vue": "components/Register.vue",
    "tests/example.spec.js": "tests/example.spec.js",
    "tests/components/Footer.spec.js": "tests/Footer.spec.js",
    "tests/components/Header.spec.js": "tests/Header.router.spec.js",
    "tests/components/Home.spec.js": "tests/Home.store.spec.js",
}
for lab in ("lab22", "lab23", "lab24"):
    MAP[f"solutions/{lab}"] = dict(_LAB22)

# labs/lab03/conduit is the untouched starter project students clone.
# These two are freshly-scaffolded starter projects: Header.vue is what the
# student writes in Lab 03, so it must NOT be shipped here.
MAP["labs/lab03/conduit"] = {
    "src/main.js": "main.lab03.js",
    "src/App.vue": "App.starter.vue",
    "src/components/HelloWorld.vue": "components/HelloWorld.vue",
}
MAP["setup-test"] = {
    "src/main.js": "main.lab03.js",
    "src/App.vue": "App.starter.vue",
    "src/components/HelloWorld.vue": "components/HelloWorld.vue",
    "tests/example.spec.js": "tests/example.spec.js",
}

# Files that no longer exist in the Vue 3 tree.
OBSOLETE = [
    "src/store", "src/mixins", "tests/unit",
]

def main():
    for proj, files in MAP.items():
        d = os.path.join(ROOT, proj)
        if not os.path.isdir(d):
            print("SKIP (missing):", proj); continue
        for junk in OBSOLETE:
            p = os.path.join(d, junk)
            if os.path.isdir(p):
                shutil.rmtree(p)
        for dest, src in files.items():
            s = os.path.join(SRC, src)
            if not os.path.exists(s):
                sys.exit(f"missing source {s} (for {proj}/{dest})")
            t = os.path.join(d, dest)
            os.makedirs(os.path.dirname(t), exist_ok=True)
            shutil.copyfile(s, t)
        print("applied:", proj, f"({len(files)} files)")

if __name__ == "__main__":
    main()

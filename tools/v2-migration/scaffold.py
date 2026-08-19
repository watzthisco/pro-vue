#!/usr/bin/env python3
"""Generate Vite/Vue 3 scaffolding for each solution + lab project."""
import json, os, sys

ROOT = "/home/user/pro-vue"

VERSIONS = {
    "vue": "^3.5.41",
    "vue-router": "^5.2.0",
    "pinia": "^4.0.3",
    "axios": "^1.19.0",
    "vite": "^8.2.1",
    "@vitejs/plugin-vue": "^6.0.8",
    "vitest": "^4.1.11",
    "jsdom": "^30.0.1",
    "@vue/test-utils": "^2.4.11",
    "eslint": "^10.8.1",
    "eslint-plugin-vue": "^10.10.0",
    "@vitest/eslint-plugin": None,   # filled in at runtime if desired
    "globals": "^17.11.0",
    "@eslint/js": "^10.0.1",
}

# lab -> feature flags
PROJECTS = {
    "solutions/lab03": dict(tests=False, axios=False, pinia=False, router=False),
    "solutions/lab04": dict(tests=False, axios=False, pinia=False, router=False),
    "solutions/lab05": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab11": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab12": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab13": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab14": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab15": dict(tests=True,  axios=False, pinia=False, router=False),
    "solutions/lab16": dict(tests=True,  axios=True,  pinia=False, router=False),
    "solutions/lab17": dict(tests=True,  axios=True,  pinia=False, router=False),
    "solutions/lab18": dict(tests=True,  axios=True,  pinia=False, router=False),
    "solutions/lab19": dict(tests=True,  axios=True,  pinia=False, router=False),
    "solutions/lab20": dict(tests=True,  axios=True,  pinia=True,  router=False),
    "solutions/lab21": dict(tests=True,  axios=True,  pinia=True,  router=True),
    "solutions/lab22": dict(tests=True,  axios=True,  pinia=True,  router=True),
    "solutions/lab23": dict(tests=True,  axios=True,  pinia=True,  router=True),
    "solutions/lab24": dict(tests=True,  axios=True,  pinia=True,  router=True),
    "labs/lab03/conduit": dict(tests=False, axios=False, pinia=False, router=False),
    "setup-test": dict(tests=True, axios=False, pinia=False, router=False),
}

def package_json(name, flags):
    deps = {"vue": VERSIONS["vue"]}
    if flags["axios"]:
        deps["axios"] = VERSIONS["axios"]
    if flags["pinia"]:
        deps["pinia"] = VERSIONS["pinia"]
    if flags["router"]:
        deps["vue-router"] = VERSIONS["vue-router"]

    dev = {
        "@eslint/js": VERSIONS["@eslint/js"],
        "@vitejs/plugin-vue": VERSIONS["@vitejs/plugin-vue"],
        "eslint": VERSIONS["eslint"],
        "eslint-plugin-vue": VERSIONS["eslint-plugin-vue"],
        "globals": VERSIONS["globals"],
        "vite": VERSIONS["vite"],
    }
    scripts = {
        "dev": "vite",
        "serve": "vite",
        "build": "vite build",
        "preview": "vite preview",
        "lint": "eslint . --fix",
    }
    if flags["tests"]:
        dev["@vue/test-utils"] = VERSIONS["@vue/test-utils"]
        dev["jsdom"] = VERSIONS["jsdom"]
        dev["vitest"] = VERSIONS["vitest"]
        scripts["test"] = "vitest run"
        scripts["test:unit"] = "vitest run"
        scripts["test:watch"] = "vitest"

    return {
        "name": name,
        "version": "2.0.0",
        "private": True,
        "type": "module",
        "engines": {"node": "^20.19.0 || >=22.12.0"},
        "scripts": dict(sorted(scripts.items())),
        "dependencies": dict(sorted(deps.items())),
        "devDependencies": dict(sorted(dev.items())),
    }

VITE_CONFIG = """import {{ fileURLToPath, URL }} from 'node:url';

import {{ defineConfig }} from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vite.dev/config/
export default defineConfig({{
  plugins: [vue()],
  resolve: {{
    alias: {{
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    }},
  }},
{test}}});
"""

VITE_TEST_BLOCK = """  test: {
    environment: 'jsdom',
    globals: true,
    include: ['tests/**/*.spec.js'],
  },
"""

ESLINT_CONFIG_BASE = """import js from '@eslint/js';
import pluginVue from 'eslint-plugin-vue';
import globals from 'globals';

export default [
  {
    ignores: ['dist/**', 'node_modules/**', 'coverage/**'],
  },
  js.configs.recommended,
  ...pluginVue.configs['flat/essential'],
  {
    files: ['**/*.{js,vue}'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      // The Conduit components deliberately use single-word names
      // (Header, Footer, Home) to match the RealWorld reference markup.
      'vue/multi-word-component-names': 'off',
    },
  },
%TESTS%];
"""

ESLINT_TEST_BLOCK = """  {
    files: ['tests/**/*.js'],
    languageOptions: {
      globals: {
        ...globals.node,
        describe: 'readonly',
        it: 'readonly',
        expect: 'readonly',
        beforeEach: 'readonly',
        afterEach: 'readonly',
        vi: 'readonly',
      },
    },
  },
"""

INDEX_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" href="/favicon.ico" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
      rel="stylesheet"
      crossorigin="anonymous"
    />
    <title>conduit</title>
  </head>
  <body>
    <noscript>
      <strong
        >We're sorry but conduit doesn't work properly without JavaScript
        enabled. Please enable it to continue.</strong
      >
    </noscript>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def main():
    for rel, flags in PROJECTS.items():
        d = os.path.join(ROOT, rel)
        if not os.path.isdir(d):
            print("SKIP (missing):", rel); continue
        name = "conduit"
        write(os.path.join(d, "package.json"),
              json.dumps(package_json(name, flags), indent=2) + "\n")
        write(os.path.join(d, "vite.config.js"),
              VITE_CONFIG.format(test=VITE_TEST_BLOCK if flags["tests"] else ""))
        write(os.path.join(d, "eslint.config.js"),
              ESLINT_CONFIG_BASE.replace("%TESTS%", ESLINT_TEST_BLOCK if flags["tests"] else ""))
        write(os.path.join(d, "index.html"), INDEX_HTML)
        # remove obsolete files
        for junk in ("babel.config.js", "jest.config.js", "public/index.html",
                     "tests/unit/.eslintrc.js", ".eslintrc.js", "package-lock.json"):
            p = os.path.join(d, junk)
            if os.path.exists(p):
                os.remove(p)
        print("scaffolded:", rel)

if __name__ == "__main__":
    main()

import js from "@eslint/js";
import globals from "globals";
export default [
  {
    ignores: ["node_modules/**", "eslint.config.js"],
  },
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      indent: ["error", 4],
      "linebreak-style": ["error", "unix"],
      quotes: ["error", "single"],
      semi: ["error", "always"],
      "no-console": "warn",
    },
  },
];

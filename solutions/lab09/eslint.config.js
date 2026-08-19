import js from '@eslint/js';
import globals from 'globals';

// ESLint 9 and later use this "flat config" format. The file is an array of
// configuration objects; each one applies to the files it matches.
export default [
  {
    // The config file itself follows Prettier-style 2-space indentation,
    // so exclude it from the 4-space rule this lab configures.
    ignores: ['node_modules/**', 'eslint.config.js'],
  },
  js.configs.recommended,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      indent: ['error', 4],
      'linebreak-style': ['error', 'unix'],
      quotes: ['error', 'single'],
      semi: ['error', 'always'],
      'no-console': 'warn',
    },
  },
];

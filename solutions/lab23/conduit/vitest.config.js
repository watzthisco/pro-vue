import { fileURLToPath } from 'node:url'
import { mergeConfig, defineConfig, configDefaults } from 'vitest/config'
import viteConfig from './vite.config.js'

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      environment: 'jsdom',
      exclude: [...configDefaults.exclude, 'e2e/**'],
      root: fileURLToPath(new URL('./', import.meta.url)),
      coverage: {
        provider: 'v8',
        include: ['src/**/*.{js,vue}'],
        // Unused scaffold icons and the sample JSON are not application logic.
        exclude: ['src/components/icons/**', 'src/json/**'],
        reporter: ['text', 'html'],
      },
    },
  }),
)

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// Vite needs no loader rules: it understands .vue files through this plugin
// and serves everything else as native ES modules during development.
export default defineConfig({
  plugins: [vue()],
});

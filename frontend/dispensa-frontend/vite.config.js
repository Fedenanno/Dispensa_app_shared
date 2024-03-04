import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'
import mkcert from 'vite-plugin-mkcert'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      injectRegister: 'auto',
      registerType: 'autoUpdate',//injectManifest
      // srcDir: '/',
      // filename: 'sw.js',
      devOptions: {
        enabled: true
      },
      manifest: {
        name: 'Dispensa',
        description: 'Dispensa is a simple app to manage your groceries',
        short_name: 'Dispensa',
        theme_color: '#ffffff',
        icons: [
          {
            src: 'icon_pwa/192_icon.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'icon_pwa/512_icon.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
          
      },
    }),
    mkcert(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: true,
    https: false,
  }
})

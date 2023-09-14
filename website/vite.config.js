import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
    ],
    resolve: {
        alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
        }
  },
    // 反向代理设置
    server: {
        proxy: {
            '/api': { 
                target: 'https://127.0.0.1:8085', // 目标地址 --> 服务器地址
                changeOrigin: true, // 允许跨域
                ws: true,  // 允许websocket代理
                // 重写路径 --> 作用与vue配置pathRewrite作用相同
                rewrite: (path) => path.replace(/^\/api/, "")
            }
        },
    },
})

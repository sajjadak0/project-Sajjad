import { defineConfig } from "vite";
import { resolve } from "node:path";

export default defineConfig({
  root: ".",
  build: {
    outDir: resolve(import.meta.dirname, "..", "static", "dist"),
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: {
        "alpine-entry": resolve(__dirname, "src/entry/alpine-entry.ts"),
        "bootstrap-entry": resolve(__dirname, "src/entry/bootstrap-entry.ts"),
      },
      output: {
        entryFileNames: "[name].[hash].js",
        chunkFileNames: "chunks/[name].[hash].js",
        assetFileNames: "assets/[name].[hash].css"
      },
    },
  },
  server: {
    host: "127.0.0.1",
    port: 5173,
    strictPort: true,
  },
});

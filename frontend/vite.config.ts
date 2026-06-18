import { defineConfig } from "vite";
import { resolve } from "node:path";

export default defineConfig({
  root: ".",
  build: {
    outDir: resolve(import.meta.dirname, "..", "static", "dist"),
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: "src/entry/alpine-entry.ts",
      output: {
        entryFileNames: "[name].[hash].js",
        chunkFileNames: "chunks/[name].[hash].js",
      },
    },
  },
  server: {
    host: "127.0.0.1",
    port: 5173,
    strictPort: true,
  },
});

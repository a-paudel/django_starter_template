import { defineConfig } from "vite";
import * as path from "path";

export default defineConfig({
    base: "/static/",
    publicDir: "resources/public",
    build: {
        manifest: true,
        outDir: path.resolve(__dirname, "staticfiles"),
        copyPublicDir: true,
        rollupOptions: {
            input: ["resources/js/app.ts"],
        },
    },
});

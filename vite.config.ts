import { defineConfig } from "vite";
import * as path from "path";
import tailwindcss from "@tailwindcss/vite";

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
    plugins: [
        //
        tailwindcss(),
    ],
});

// Add this at the beginning of your app entry.
import "vite/modulepreload-polyfill";
import "../css/main.css";
import Alpine from "alpinejs";

// @ts-ignore
window.Alpine = Alpine;
Alpine.start();

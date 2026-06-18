import Alpine from "alpinejs";
import { logtest } from "../components/sepehr";

declare global {
  interface Window {
    Alpine: typeof Alpine;
  }
}

document.addEventListener("alpine:init", function () {
  Alpine.data("logtest", logtest);
});

window.Alpine = Alpine;
Alpine.start();

import { createApp } from "https://unpkg.com/vue@3.2.4/dist/vue.esm-browser.prod.js";
const app = createApp({
    delimiters: ["${", "}"],
    el:"#app",
    data: {
        message: "lorem ipsum"
    }
});
app.mount("#app");
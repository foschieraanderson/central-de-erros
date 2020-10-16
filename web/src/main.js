import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

require('@/assets/styles/global.css');

createApp(App)
  .use(router)
  .mount("#app");

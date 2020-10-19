<template>
  <Sidebar />
  <div class="home">
    <p>Bem vindo {{ user.token }}</p>
    <ul>
      <li v-for="log in logs" :key="log.id" >Título: {{ log.title }}</li>
    </ul>
  </div>
</template>

<script>

import api from "../services/api";
import { authHeader } from "../services/AuthHeader";

import Sidebar from "../components/Sidebar.vue";

export default {
  name: "Home",
  components: {
    Sidebar
  },
  data() {
    return {
      user: localStorage.getItem("user"),
      logs: [],
    }
  },
  mounted() {
    const token = authHeader();

    api.get("logs/", { headers: token })
    .then(res => {
      this.logs = res.data;
    })
  },

};
</script>

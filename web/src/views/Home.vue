<template>
  <!-- <Sidebar :username="user.user.username" :token="user.token" /> -->
  <Sidebar :username="user.user.username" />
  <div class="home">
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
      user: JSON.parse(localStorage.getItem("user")),
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

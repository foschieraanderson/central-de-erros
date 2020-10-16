<template>
  <div class="home">
    <ul>
      <li v-for="log in logs" :key="log.id" >Título: {{ log.title }}</li>
    </ul>
  </div>
</template>

<script>

import api from "../services/api";
import { authHeader } from "../services/AuthHeader";

export default {
  name: "Home",
  data() {
    return {
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

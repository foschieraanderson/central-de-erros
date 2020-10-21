<template>
    <section id="sidebar">
      <div class="sidebar-box-info">
        <h2>Bem vindo {{ username }}.</h2>
        <p>Seu token é: {{ token }}</p>
      </div>
      <div class="sidebar-box-profile">
        <button @click="handleLogout">Sair</button>
      </div>
      <!-- <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> -->
  </section>
</template>

<script>

export default {
  props: {
    "username": String,
    "token": String,
  },
  methods: {
    handleLogout() {
      localStorage.removeItem("user");
      this.$router.push("/login");
    }
  },
}
</script>
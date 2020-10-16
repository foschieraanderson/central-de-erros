<template>
    <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
    <button @click="handleLogout">Sair</button>
  </div>
</template>

<script>

export default {
  methods: {
    handleLogout() {
      localStorage.removeItem("user");
      this.$router.push("/login");
    }
  },
}
</script>
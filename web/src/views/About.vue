<template>
  <Sidebar />
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>

import Sidebar from "../components/Sidebar.vue";

export default {
  name: "About",
  components: {
    Sidebar
  }
}
</script>

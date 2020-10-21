<template>
  <!-- <Sidebar :username="user.user.username" :token="user.token" /> -->
  <Sidebar :username="capitalize" :token="truncate" />
  <section id="filters">
    <form>
      <select name="origin" id="origin">
        <option value="producao">Produção</option>
        <option value="homologacao">Homologação</option>
        <option value="dev">Dev</option>
      </select>

      <select name="order" id="order">
        <option value="">Ordenar por</option>
        <option value="level">Level</option>
        <option value="frequencia">Frequência</option>
      </select>

      <select name="buscar" id="buscar">
        <option value="">Buscar por</option>
        <option value="level">Level</option>
        <option value="descricao">Descrição</option>
        <option value="origin">Origem</option>
      </select>

      <input type="text" name="search" id="search" />
    </form>
  </section>

  <header>
    <button>Arquivar</button>
    <button>Apagar</button>
  </header>

  <table>
    <thead>
      <tr>
        <th><input type="checkbox" name="check" id="check"></th>
        <th>Level</th>
        <th>Log</th>
        <th>Eventos</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="log in logs" :key="log.id">
        <td><input type="checkbox" name="{{ log.id }}" id="{{ log.id }}"></td>
        <td><p>{{ log.level }}</p></td>
        <td>{{ log.description }}<br/>{{ log.origin }}<br/>{{ log.created_at }}</td>
        <td>{{ log.events }}</td>
      </tr>
    </tbody>
  </table>
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
  computed: {
    capitalize: function() {
      const value = this.user.user.username.toString()
      return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase()
    },
    truncate: function() {
      const value = this.user.token.toString()
      return value.substring(0, 32) + "..." 
    },
    // dateTime: function() {
    //   const date = this.user.user.created_at
    //   return date.toLocaleDateString()
    // }
  },

};
</script>
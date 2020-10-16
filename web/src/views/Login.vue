<template>
    <div>
        <h2>Login</h2>
        <form @submit="handleSubmit">
            <div>{{ erro }}</div>
            <div>
                <label for="email">E-mail</label>
                <input v-model="email" type="email" name="email" id="email">
            </div>
            <div>
                <label for="password">Senha</label>
                <input v-model="password" type="password" name="password" id="password">
            </div>
            <div>
                <button>Entrar</button>
                <router-link to="/register">Registrar-se</router-link>
            </div>
        </form>
    </div>
</template>

<script>

import api from "../services/api";

export default {
    name: "Login",
    data() {
        return {
            erro: "",
            email:"",
            password:"",
            submitted: false
        };
    },
    methods: {
        handleSubmit(e) {
            e.preventDefault();

            const options = {"email": this.email, "password": this.password};
        
            api.post("auth/token/", options)
            .then(res => {
                if (res.data.token) {
                    localStorage.setItem("user", JSON.stringify(res.data));
                    this.$router.push('/');
                }
            })
            .catch(() => {
                alert("Erro ao efetuar o login, tente novamente.");
            })
        }
    },
};
</script>

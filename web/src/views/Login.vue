<template>
    <section class="form-container">
        <h1>Login</h1>
        <form @submit="handleSubmit">
            <input v-model="email" type="email" name="email" id="email" placeholder="e-mail">
            <input v-model="password" type="password" name="password" id="password" placeholder="password">
            <div class="form-buttons">
                <button type="submit">Login</button>
                <router-link to="/register">Registrar-se</router-link>
            </div>
        </form>
    </section>
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

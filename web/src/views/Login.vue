<template>
    <section class="form-container">
        <h1>Login</h1>
        <form @submit="handleSubmit">
            <div class="badge-erros" v-for="erro in erros" :key="erro">{{ erro }}</div>
            <input v-model="email" type="email" name="email" id="email" placeholder="e-mail">
            <ul v-if="errosEmail.length">
                <li class="label-erros" v-for="erro in errosEmail" :key="erro">{{ erro }}</li>
            </ul>
            <input v-model="password" type="password" name="password" id="password" placeholder="password">
            <ul v-if="errosPassword.length">
                <li class="label-erros" v-for="erro in errosPassword" :key="erro">{{ erro }}</li>
            </ul>
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
            erros: [],
            errosEmail: [],
            errosPassword: [],
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
            .catch(err => {
                if (err.response.data.email) {
                    this.errosEmail = err.response.data.email
                }

                if (err.response.data.password) {
                    this.errosPassword = err.response.data.password
                }

                if (err.response.data.non_field_errors) {
                    this.erros = err.response.data.non_field_errors
                }
            })
        }
    },
};
</script>

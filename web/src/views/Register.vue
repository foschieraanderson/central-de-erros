<template>
    <section class="form-container">
        <h1>Cadastro</h1>
        <form @submit="handleRegister">
            <div class="badge-erros" v-for="erro in erros" :key="erro">{{ erro }}</div>
            <input v-model="username" type="username" name="username" id="username" placeholder="username">
            <ul v-if="errosUsername.length">
                <li class="label-erros" v-for="erro in errosUsername" :key="erro">{{ erro }}</li>
            </ul>
            <input v-model="email" type="email" name="email" id="email" placeholder="e-mail">
            <ul v-if="errosEmail.length">
                <li class="label-erros" v-for="erro in errosEmail" :key="erro">{{ erro }}</li>
            </ul>
            <input v-model="password" type="password" name="password" id="password" placeholder="password">
            <ul v-if="errosPassword.length">
                <li class="label-erros" v-for="erro in errosPassword" :key="erro">{{ erro }}</li>
            </ul>
            <div class="form-buttons">
                <button type="submit">Cadastrar</button>
            </div>
        </form>
    </section>
</template>

<script>

import api from "../services/api";

export default {
    name: "Register",
    data() {
        return {
            erros: [],
            errosUsername: [],
            errosEmail: [],
            errosPassword: [],
            username:'',
            email:'',
            password:'',
            submitted: false
        }
    },
    methods: {
        handleRegister(e) {
            e.preventDefault();
            
            const data = {
                "username": this.username,
                "email": this.email,
                "password": this.password
            };

            api.post("auth/register/", data)
            .then(res => {
                if (res.data.email) {
                    this.$router.push("/login");
                }
            })
            .catch(err => {
                if (err.response.data.username) {
                    this.errosUsername = err.response.data.username
                }

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
}
</script>

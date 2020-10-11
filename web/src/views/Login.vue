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
                <a href="#">Registrar-se</a>
            </div>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/v1/';

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
        
            axios.post(baseURL + "auth/token/", options)
            .then(res => {
                console.log(res.data.token);
                if (res.data.token) {
                    localStorage.setItem("user", JSON.stringify(res.data));
                    this.$router.push('/');
                }
            })
            .catch(err => {
                this.erro = err.data.email;
            })
        }
    },
};
</script>

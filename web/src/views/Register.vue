<template>
    <div>
        <h2>Register</h2>
        <form @submit="handleRegister">
            <div>
                <label for="username">Username</label>
                <input v-model="username" type="username" name="username" id="username">
            </div>
            <div>
                <label for="email">E-mail</label>
                <input v-model="email" type="email" name="email" id="email">
            </div>
            <div>
                <label for="password">Senha</label>
                <input v-model="password" type="password" name="password" id="password">
            </div>
            <div>
                <button>Registrar</button>
                <router-link to="/login">Login</router-link>
            </div>
        </form>
    </div>
</template>

<script>

import api from "../services/api";

export default {
    name: "Register",
    data() {
        return {
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
                console.log(err);
            })

        }
    },
}
</script>

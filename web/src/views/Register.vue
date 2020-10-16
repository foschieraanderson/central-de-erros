<template>
    <section class="form-container">
        <h1>Cadastro</h1>
        <form @submit="handleRegister">
            <input v-model="username" type="username" name="username" id="username" placeholder="username">
            <input v-model="email" type="email" name="email" id="email" placeholder="e-mail">
            <input v-model="password" type="password" name="password" id="password" placeholder="password">
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

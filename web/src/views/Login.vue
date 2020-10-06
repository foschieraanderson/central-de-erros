<<template>
    <div>
        <h2>Login</h2>
        <form>
            <div>
                <label for="email">E-mail</label>
                <input type="email" name="email" id="email">
                <div>E-mail é obrigatório</div>
            </div>
            <div>
                <label for="password">Senha</label>
                <input type="password" name="password" id="password">
                <div>Senha é obrigatório</div>
            </div>
            <div>
                <button>Entrar</button>
                <a href="#">Registrar-se</a>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email:'',
            password:'',
            submitted: false
        }
    },
}
</script>

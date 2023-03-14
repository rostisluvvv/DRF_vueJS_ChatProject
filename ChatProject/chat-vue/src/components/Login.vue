<template>
  <div>
    <input v-model="login" type="text" placeholder="Логин" />
    <input v-model="password" type="password" placeholder="Пароль" />
    <button @click="setLogin">Войти</button>
  </div>
</template>
<script>
import 'whatwg-fetch';

export default {
  name: 'Login',
  data() {
    return {
      login: '',
      password: '',
    };
  },
  methods: {
    setLogin() {
      const data = new URLSearchParams();
      data.append('username', this.login);
      data.append('password', this.password);

      fetch('http://127.0.0.1:8000/auth/token/create/', {
        method: 'POST',
        headers: {},
        body: data,
      })
        .then((response) => {
          if (response.status === 400) {
            alert('Логин или пароль неверен');
          } else if (response.status === 200) {

            response.json().then(data=>{
                    alert('Авторизация успешна');
            sessionStorage.setItem("auth_token", data.data.attributes.auth_token)
            });

          }
        });
    },
  },
};
</script>
<style scoped>

</style>

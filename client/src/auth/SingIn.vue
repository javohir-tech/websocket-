<template>
  <div class="auth-page">
    <div class="glow glow-1"></div>
    <div class="glow glow-2"></div>

    <div class="auth-card">
      <div class="auth-header">
        <div class="logo-wrap">
          <span class="logo-icon">⬡</span>
        </div>
        <h1>Kirish</h1>
        <p>Xush kelibsiz</p>
      </div>

      <form @submit.prevent="handleLogin" class="auth-form" autocomplete="off">
        <div class="field">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            placeholder="Username"
            autocomplete="off"
            required
          />
        </div>

        <div class="field">
          <label for="password">Parol</label>
          <input
            id="password"
            v-model="form.password"
            :type="showPass ? 'text' : 'password'"
            placeholder="Parolingiz"
            autocomplete="new-password"
            required
          />
          <button type="button" class="eye-btn" @click="showPass = !showPass">
            {{ showPass ? '🙈' : '👁️' }}
          </button>
        </div>

        <p v-if="errorMsg" class="error-msg">⚠ {{ errorMsg }}</p>

        <button type="submit" class="submit-btn" :disabled="loading">
          <span v-if="loading" class="loader"></span>
          <span v-else>Kirish</span>
        </button>

        <p class="auth-link">
          Akkauntingiz yo'qmi? <RouterLink to="singup">Ro'yxatdan o'tish</RouterLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const form = reactive({ username: '', password: '' })
const showPass = ref(false)
const loading = ref(false)
const errorMsg = ref('')

const handleLogin = async () => {
  errorMsg.value = ''
  loading.value = true
  try {
    // === API logikangizni shu yerga yozing ===
    // const res = await authService.login(form)
    // router.push('/chat')
    console.log('Login data:', form)
  } catch (err) {
    errorMsg.value = err?.message || 'Username yoki parol noto\'g\'ri'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import '../assets/auth.css';
</style>
<template>
  <div class="auth-page">
    <div class="glow glow-1"></div>
    <div class="glow glow-2"></div>

    <div class="auth-card">
      <div class="auth-header">
        <div class="logo-wrap">
          <span class="logo-icon">⬡</span>
        </div>
        <h1>Sign Up</h1>
        <p>Akkaunt yarating</p>
      </div>

      <form @submit.prevent="handleSignUp" class="auth-form" autocomplete="off">
        <div class="field">
          <label for="name">Ism</label>
          <input
            id="name"
            v-model="form.name"
            type="text"
            placeholder="Ismingiz"
            autocomplete="off"
            required
          />
        </div>

        <div class="field">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="email@example.com"
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
            placeholder="Kamida 6 ta belgi"
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
          <span v-else>Ro'yxatdan o'tish</span>
        </button>

        <p class="auth-link">
          Akkauntingiz bormi? <RouterLink to="singin">Kirish</RouterLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const form = reactive({ name: '', email: '', password: '' })
const showPass = ref(false)
const loading = ref(false)
const errorMsg = ref('')

const handleSignUp = async () => {
  errorMsg.value = ''
  loading.value = true
  try {
    // === API logikangizni shu yerga yozing ===
    // const res = await authService.signUp(form)
    // router.push('/chat')
    console.log('SignUp data:', form)
  } catch (err) {
    errorMsg.value = err?.message || 'Xatolik yuz berdi'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import '../assets/auth.css';
</style>
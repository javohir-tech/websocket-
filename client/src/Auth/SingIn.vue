<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Welcome back</h1>
      <p class="auth-subtitle">Davom etish uchun tizimga kiring</p>

      <form class="auth-form" @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            placeholder="username"
            required
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            placeholder="••••••••"
            required
          />
        </div>

        <button type="submit" class="submit-btn">Sign In</button>
      </form>

      <p class="auth-footer">
        Akkauntingiz yo'qmi?
        <RouterLink to="singup">Sign Up</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { RouterLink } from 'vue-router'
import '@/assets/auth.css'

const form = reactive({
  username: '',
  password: '',
})

function handleSubmit() {
  const data = { ...form }
  // API logikangizni shu yerda yozing
  console.log('Login data:', data)
}
</script>
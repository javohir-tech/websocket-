<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Create account</h1>
      <p class="auth-subtitle">Ro'yxatdan o'tish uchun ma'lumotlarni kiriting</p>

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
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="email@example.com"
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

        <button type="submit" class="submit-btn">Sign Up</button>
      </form>

      <p class="auth-footer">
        Akkauntingiz bormi?
        <RouterLink to="/singin">Sign In</RouterLink>
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
  email: '',
  password: '',
})

function handleSubmit() {
  const data = { ...form }
  // API logikangizni shu yerda yozing
  console.log('Signup data:', data)
}
</script>
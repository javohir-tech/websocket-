<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Welcome back</h1>
      <p class="auth-subtitle">Davom etish uchun tizimga kiring</p>

      <form class="auth-form" @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username</label>
          <input id="username" v-model="form.username" type="text" placeholder="username" required />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" v-model="form.password" type="password" placeholder="••••••••" required />
        </div>

        <button type="submit" class="submit-btn" :disabled="loading">{{ loading ? "Loading..." : "Sign In" }}</button>
      </form>

      <p class="auth-footer">
        Akkauntingiz yo'qmi?
        <RouterLink to="singup">Sign Up</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import '@/assets/auth.css'
import api from '@/utils/axios'
import { toast } from 'vue3-toastify'


const loading = ref(false)
const router = useRouter()

const form = reactive({
  username: '',
  password: '',
})

async function handleSubmit() {
  loading.value = true
  try {
    const { data } = await api.post("/auth/singin/", form)

    localStorage.setItem("username", data.data.username)
    localStorage.setItem("email", data.data.email)
    localStorage.setItem('access_token', data.data.tokens.access_token)
    localStorage.setItem('refresh_token', data.data.tokens.refresh_token)
    router.push("/")
    // console.log(data)
  } catch (error) {
    if (error.response) {
      const data = error.response.data
      if (data.user) {
        toast.error(data.user[0])
      }
      console.log(error.response)
    } else {
      console.log(error)
    }
  } finally {
    loading.value = false
  }
}
</script>
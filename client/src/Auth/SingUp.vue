<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Create account</h1>
      <p class="auth-subtitle">Ro'yxatdan o'tish uchun ma'lumotlarni kiriting</p>

      <form class="auth-form" @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username</label>
          <input id="username" v-model="form.username" type="text" placeholder="username" required />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" v-model="form.email" type="email" placeholder="email@example.com" required />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" v-model="form.password" type="password" placeholder="••••••••" required />
        </div>

        <button type="submit" class="submit-btn" :disabled="loading">{{ loading ? "Loading..." : "Sign Up" }}</button>
      </form>

      <p class="auth-footer">
        Akkauntingiz bormi?
        <RouterLink to="/singin">Sign In</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { RouterLink } from 'vue-router'
import '@/assets/auth.css'
import api from '@/utils/axios'
import { useRouter } from 'vue-router'
import { toast } from 'vue3-toastify';
import { useUserStore } from '@/stores/user'

const form = reactive({
  username: '',
  email: '',
  password: '',
})

const userStore = useUserStore()
const router = useRouter()
const loading = ref(false)

async function handleSubmit() {
  loading.value = true
  try {
    const { data } = await api.post("/auth/singup/", form)

    localStorage.setItem("username", data.username)
    localStorage.setItem("email", data.email)
    localStorage.setItem('access_token', data.tokens.access_token)
    localStorage.setItem('refresh_token', data.tokens.refresh_token)
    userStore.addToken(data.tokens.access_token)
    router.push("/")
    // console.log(data)
  } catch (error) {
    if(error.response){
      const data = error.response.data
      if(data.email){
        toast.error(data.email[0])
      }else if(data.username){
        toast.error(data.username[0])
      }
      console.log(error.response)
    }else{
      console.log(error)
    }
  } finally {
    loading.value = false
  }
}
</script>
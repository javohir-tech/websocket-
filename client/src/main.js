import { createApp } from 'vue'
import './style.css'
import 'vue3-toastify/dist/index.css';
import App from './App.vue'
import router from './Router'
import Vue3Toastify from 'vue3-toastify';


const app = createApp(App)
app.use(Vue3Toastify , {
    autoClose : 3000
})
app.use(router)
app.mount('#app')

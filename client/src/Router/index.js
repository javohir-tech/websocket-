import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/Layout/mainLayout.vue'
import { SingIn, SingUp } from '@/Auth'
import { ChatView, HomeView } from '@/views'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: MainLayout,
      children: [
        /////// Auth ////////////
        {
          path: "singup",
          component: SingUp
        },
        {
          path: "singin",
          component: SingIn
        },

        //// Views ////
        {
          path: "",
          component: HomeView
        },
        {
          path: "chats",
          component: ChatView
        }
      ]
    }
  ],
})

export default router

import { createRouter, createWebHistory } from "vue-router"
import MainLayout from "../Layout/mainLayout.vue"

/////////////////// Auth //////////////////
import { SingIn, SingUp } from "../auth"
import { Chat, Home } from "../Views"

const router = createRouter({
    history: createWebHistory(import.meta.env.API_URL),
    routes: [
        {
            path: "/",
            component: MainLayout,
            children: [
                ////// Auth ///////
                {
                    path: "singup",
                    component: SingUp
                },
                {
                    path: "singin",
                    component: SingIn
                },
                ////// views ///////
                {
                    path: "",
                    component: Home
                },
                {
                    path: "chat",
                    component: Chat
                }
            ]
        }
    ]
})

export default router
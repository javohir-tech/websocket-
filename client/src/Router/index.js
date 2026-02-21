import { createRouter, createWebHistory } from "vue-router"
import MainLayout from "../Layout/mainLayout.vue"

/////////////////// Auth //////////////////
import { SingIn, SingUp } from "../auth"

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
                }
                ////// views ///////
            ]
        }
    ]
})

export default router
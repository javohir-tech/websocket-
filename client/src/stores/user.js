import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
    state: () => ({
        token: localStorage.getItem("access_token") || null
    }),
    actions: {
        addToken(token) {
            this.token = token
        }
    }
})
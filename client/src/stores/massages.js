import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', {
    state: () => (
        {
            message: null
        }
    ),
    getters: {
        unReadCount: (state) => 0
    },

    actions: {
        on_message(data) {
            this.message = data
        }
    }
})
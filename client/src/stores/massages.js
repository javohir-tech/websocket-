import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', {
    state: () => (
        {
            message: []
        }
    ),
    getters: {
        unReadCount: (state) => state.message.length ?? 0
    },
    
    actions: {
        on_message(data) {
            this.message = data
        }
    }
})
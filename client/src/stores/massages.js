import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', {
    state: () => (
        {
            unread_messages: []
        }
    ),
    getters: {
        unReadCount: (state) =>  state.unread_messages.length
    },

    actions: {
        on_message(data) {
            this.unread_messages.push(data)
        }
    }
})
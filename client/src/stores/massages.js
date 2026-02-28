import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', {
    state: () => (
        {
            unread_messages: []
        }
    ),

    actions: {
        on_message(data) {
            this.unread_messages.push(data)
        }
    }
})
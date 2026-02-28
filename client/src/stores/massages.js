import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', {
    state: () => (
        {
            unread_messages: {}
        }
    ),
    getters: {
        unReadCount: (state) => Object.keys(state.unread_messages).length
    },

    actions: {
        on_message(data) {
            const sender = data.sender
            console.log(sender)
            if (!this.unread_messages[sender]) {
                this.unread_messages[sender] = [data]
            } else {
                this.unread_messages[sender].push(data)
            }
        }
    }
})
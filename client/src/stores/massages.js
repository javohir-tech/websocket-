import { defineStore } from "pinia";

export const useChatStore = defineStore('chat', () => {
    state : ()=>(
        {
            unread_messages : []
        }
    )

    actions : {
        
    }
})
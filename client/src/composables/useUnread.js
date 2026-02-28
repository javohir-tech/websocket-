import { ref } from "vue";
import { useChatStore } from "@/stores/massages";

const messages = ref([])
const ws = ref(null)
const isConnected = ref(false)

export function UnReadChats() {
    const chatStore = useChatStore()

    function connect() {
        const token = localStorage.getItem("access_token")

        if (!token) {
            console.log('token topilmadi')
            return
        }

        ws.value = new WebSocket(`ws://localhost:8000/ws/unread/?token=${token}`)

        ws.value.onopen = () => {
            console.log('ulandi')
            isConnected.value = true
        }

        ws.value.onmessage = (e) => {
            const data = JSON.parse(e.data)
            chatStore.on_message(data)
        }

        ws.value.onclose = () => {
            console.log("uzildi")
            isConnected.value = false
        }
    }

    return { messages, isConnected, connect }
}
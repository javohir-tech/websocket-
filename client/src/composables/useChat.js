import { ref } from "vue";

export function useChat(userId) {
    const messages = ref([])
    const ws = ref(null)
    const isConnected = ref(false)

    function connect() {
        const token = localStorage.getItem('access_token')
        
        if (!token) {
            console.error("Token topilmadi")
            return
        }

        if (!userId) {
            console.error("userId topilmadi")
            return
        }

        ws.value = new WebSocket(`ws://localhost:8000/ws/chat/${userId}/?token=${token}`)
        
        ws.value.onopen = () => {
            console.log("Ulandi")
            isConnected.value = true
        }

        ws.value.onmessage = (e) => {
            const data = JSON.parse(e.data)
            messages.value.push(data)
        }

        ws.value.onclose = () => {
            console.log('Uzildi')
            isConnected.value = false
        }

        ws.value.onerror = (e) => {
            console.error("WebSocket xatosi:", e)
        }
    }

    function sendMessage(text) {
        if (!text?.trim()) return

        if (ws.value?.readyState === WebSocket.OPEN) {
            ws.value.send(JSON.stringify({ message: text.trim() }))
        } else {
            console.warn("WebSocket ulanmagan")
        }
    }

    function disconnect() {
        ws.value?.close()
        ws.value = null
    }

    return { messages, isConnected, connect, sendMessage, disconnect }
}
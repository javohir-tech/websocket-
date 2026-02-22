import { ref } from "vue";

export function useChat(roomName) {
    const message = ref([])
    const ws = ref(null)

    function connect() {
        const token = localStorage.getItem('access_token')
        ws.value = new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/?token=${token}`)

        ws.value.onopen = () => {
            console.log("Ulandi")
        }

        ws.value.onmessage = (e) => {
            const data = JSON.parse(e.data)
            message.value.push(data.message)
        }

        ws.value.onclose = () => {
            console.log('Uzildi')
        }
    }

    function sendMessage(text) {
        if (ws.value && ws.value.readyState === WebSocket.OPEN) {
            ws.value.send(JSON.stringify({ message: text }))
        }
    }

    function disconnect() {
        ws.value?.close()
    }

    return { message, connect, sendMessage, disconnect }
}
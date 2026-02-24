import api from "@/utils/axios";
import { ref } from "vue";

export function useChat(roomName) {
    const message = ref([])
    const ws = ref(null)

    async function connect() {
        const token = localStorage.getItem('access_token')
        ws.value = new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/?token=${token}`)
        try {
            const { data } = await api.get('http://127.0.0.1:8000/api/chat/general/history/')
            message.value = data.map((item) => {
                return { message: item.content, author: item.author }
            })
        } catch (error) {
            console.log(error.reponse || error)
        }
        ws.value.onopen = () => {
            console.log("Ulandi")
        }

        ws.value.onmessage = (e) => {
            const data = JSON.parse(e.data)
            console.log(data)
            message.value.push(data)
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
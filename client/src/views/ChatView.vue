<template>
  <div>
    <div v-for="(msg, i) in messages" :key="i">
      {{ msg }}
    </div>

    <input v-model="newMessage" @keyup.enter="send" placeholder="Xabar yoz..." />
    <button @click="send">Yuborish</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useChat } from '@/composables/useChat'

const { messages, connect, sendMessage, disconnect } = useChat('general')
const newMessage = ref('')

function send() {
  if (newMessage.value.trim()) {
    sendMessage(newMessage.value)
    newMessage.value = ''
  }
}

onMounted(() => connect())
onUnmounted(() => disconnect())
</script>


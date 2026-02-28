<script setup>
import { RouterView } from 'vue-router'
import { UnReadChats } from './composables/useUnread';
import { onMounted, watch } from 'vue';
import { useChatStore } from './stores/massages';

const chatStore = useChatStore()
const { messages, isConnected, connect } = UnReadChats()

onMounted(() => {
  connect()
  console.log(messages.value)
})

watch(()=>chatStore.unread_messages, (newVal) => {
  console.log(newVal)
} , {deep : true})
</script>

<template>
  <RouterView />
</template>

<style scoped></style>

<script setup>
import { RouterView } from 'vue-router'
import { UnReadChats } from './composables/useUnread';
import { onMounted } from 'vue';

const { messages, isConnected, connect } = UnReadChats()

onMounted(() => {
  connect()
  console.log(messages.value)
})
</script>

<template>
  <RouterView />
</template>

<style scoped></style>

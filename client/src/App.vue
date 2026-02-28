<script setup>
import { RouterView } from 'vue-router'
import { UnReadChats } from './composables/useUnread';
import { onMounted, watch } from 'vue';

const { messages, isConnected, connect } = UnReadChats()

onMounted(() => {
  connect()
})
</script>

<template>
  <RouterView />
</template>

<style scoped></style>

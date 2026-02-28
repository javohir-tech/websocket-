<template>
    <div class="chats" v-for="chat in chatStore.unread_messages" @click="handleNavigateChat(chat[chat.length-1])">
        <p>{{ chat.length }}</p>
        <p>{{ chat[chat.length-1].sender }}</p>
        <p>{{ chat[chat.length-1].message }}</p>
        <p>{{ chat[chat.length-1].created_at }}</p>
    </div>
</template>

<script setup>
import { useChatStore } from '@/stores/massages';
import { useRouter } from 'vue-router';

const router = useRouter()
const chatStore = useChatStore()

const handleNavigateChat = (sender) => {
    router.push({ name: 'chats', params: { userId: sender.sender_id , username : sender.sender }})
}
</script>

<style scoped>
.chats {
    border: solid 1px red;
    padding: 10px;
}
</style>
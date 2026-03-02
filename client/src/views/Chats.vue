<template>
  <div class="chat-container">
    <div class="header">
      <h1 class="header-title">Messages</h1>
      <span class="header-count">{{ data.length }}</span>
    </div>

    <div class="search-bar">
      <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8" />
        <path d="m21 21-4.35-4.35" />
      </svg>
      <input type="text" v-model="searchQuery" placeholder="Search conversations..." class="search-input" />
    </div>

    <div class="chat-list">
      <transition-group name="chat-item">
        <div v-for="(chat, index) in filteredChats" :key="chat.partner_id" class="chat-item"
          :style="{ animationDelay: `${index * 0.05}s` }" @click="chatTo(chat.partner_id, chat.partner)">
          <div class="avatar">
            <span class="avatar-letter">{{ chat.partner.charAt(0).toUpperCase() }}</span>
            <span class="online-dot"></span>
          </div>

          <div class="chat-content">
            <div class="chat-top">
              <span class="partner-name">{{ chat.partner }}</span>
              <span class="time">{{ formatTime(chat.last_message_time) }}</span>
            </div>
            <div class="chat-bottom">
              <span class="last-message">
                <svg v-if="chat.last_message_me" class="sent-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12" />
                </svg>
                {{ chat.last_message }}
              </span>
              <span v-if="chat.unread_count > 0" class="unread-badge">
                {{ chat.unread_count > 99 ? '99+' : chat.unread_count }}
              </span>
            </div>
          </div>
        </div>
      </transition-group>

      <div v-if="loading" class="skeleton-list">
        <div v-for="i in 5" :key="i" class="skeleton-item">
          <div class="skeleton-avatar"></div>
          <div class="skeleton-content">
            <div class="skeleton-line short"></div>
            <div class="skeleton-line long"></div>
          </div>
        </div>
      </div>

      <div v-if="!loading && filteredChats.length === 0" class="empty-state">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
        </svg>
        <p>No conversations yet</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useFetch } from '@/Hooks/useFetch';
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useChatStore } from '@/stores/massages';

const chatStore = useChatStore()
const router = useRouter();
const { getData, data, loading, err } = useFetch();
const searchQuery = ref('');

const chats = computed(() => {
  if (!chatStore.message) return data.value
  const partner_id = chatStore.message.partner_id
  const selected = data.value.find(pid => pid.partner_id === partner_id)

  if (!selected) return data.value
  
  return [
    selected,
    ...data.value.filter(
      item => item.partner_id !== partner_id
    )
  ]
})

const filteredChats = computed(() => {
  if (!chats.value) return [];
  return chats.value.filter(chat =>
    chat.partner.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    chat.last_message.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const formatTime = (isoString) => {
  if (!isoString) return '';
  const date = new Date(isoString);
  const now = new Date();
  const diff = now - date;
  const days = Math.floor(diff / 86400000);

  if (days === 0) {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  } else if (days === 1) {
    return 'Yesterday';
  } else if (days < 7) {
    return date.toLocaleDateString([], { weekday: 'short' });
  } else {
    return date.toLocaleDateString([], { month: 'short', day: 'numeric' });
  }
};

const chatTo = (userId, user) => {
  router.push({ name: 'chats', params: { userId, username: user } });
};


onMounted(() => {
  getData('/api/chats/');
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

* {
  box-sizing: border-box;
}

.chat-container {
  font-family: 'Sora', sans-serif;
  background: #0e0f14;
  min-height: 100vh;
  max-width: 480px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  color: #e8eaf0;
}

/* Header */
.header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 28px 20px 16px;
}

.header-title {
  font-size: 26px;
  font-weight: 700;
  margin: 0;
  color: #fff;
  letter-spacing: -0.5px;
}

.header-count {
  background: #5b6cff;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 20px;
  margin-top: 2px;
}

/* Search */
.search-bar {
  position: relative;
  margin: 0 16px 16px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: #555b7a;
}

.search-input {
  width: 100%;
  background: #181a24;
  border: 1px solid #252838;
  border-radius: 14px;
  padding: 11px 16px 11px 40px;
  font-family: 'Sora', sans-serif;
  font-size: 14px;
  color: #e8eaf0;
  outline: none;
  transition: border-color 0.2s;
}

.search-input::placeholder {
  color: #555b7a;
}

.search-input:focus {
  border-color: #5b6cff;
}

/* Chat List */
.chat-list {
  padding: 0 8px;
  flex: 1;
}

.chat-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 12px;
  border-radius: 16px;
  cursor: pointer;
  transition: background 0.15s ease;
  animation: fadeSlideIn 0.4s ease both;
  margin-bottom: 2px;
}

.chat-item:hover {
  background: #181a24;
}

.chat-item:active {
  background: #1e2030;
  transform: scale(0.99);
}

@keyframes fadeSlideIn {
  from {
    opacity: 0;
    transform: translateY(12px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Avatar */
.avatar {
  position: relative;
  width: 52px;
  height: 52px;
  flex-shrink: 0;
}

.avatar-letter {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg, #5b6cff, #9b59ff);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  box-shadow: 0 4px 14px rgba(91, 108, 255, 0.3);
}

.online-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 12px;
  height: 12px;
  background: #2ecc71;
  border: 2.5px solid #0e0f14;
  border-radius: 50%;
}

/* Chat Content */
.chat-content {
  flex: 1;
  min-width: 0;
}

.chat-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.partner-name {
  font-size: 15px;
  font-weight: 600;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.time {
  font-size: 12px;
  color: #555b7a;
  flex-shrink: 0;
  margin-left: 8px;
}

.chat-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.last-message {
  font-size: 13px;
  color: #7c82a0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: flex;
  align-items: center;
  gap: 4px;
}

.sent-icon {
  width: 13px;
  height: 13px;
  color: #5b6cff;
  flex-shrink: 0;
}

.unread-badge {
  background: #5b6cff;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* Skeleton */
.skeleton-list {
  padding: 8px 4px;
}

.skeleton-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px;
  margin-bottom: 4px;
}

.skeleton-avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #181a24;
  animation: shimmer 1.4s infinite;
  flex-shrink: 0;
}

.skeleton-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.skeleton-line {
  height: 12px;
  border-radius: 6px;
  background: #181a24;
  animation: shimmer 1.4s infinite;
}

.skeleton-line.short {
  width: 40%;
}

.skeleton-line.long {
  width: 75%;
}

@keyframes shimmer {

  0%,
  100% {
    opacity: 0.4;
  }

  50% {
    opacity: 0.8;
  }
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #555b7a;
  gap: 14px;
}

.empty-state svg {
  width: 48px;
  height: 48px;
}

.empty-state p {
  font-size: 15px;
  margin: 0;
}

/* Transition */
.chat-item-enter-active {
  transition: all 0.3s ease;
}

.chat-item-leave-active {
  transition: all 0.2s ease;
}

.chat-item-enter-from {
  opacity: 0;
  transform: translateX(-20px);
}

.chat-item-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
</style>
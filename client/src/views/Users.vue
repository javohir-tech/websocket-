<template>
  <div class="users-page">
    <div class="page-header">
      <div class="header-glow"></div>
      <h1 class="title">Foydalanuvchilar</h1>
      <p class="subtitle">Kimdir bilan suhbatlashmoqchisiz?</p>
    </div>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <span>Yuklanmoqda...</span>
    </div>

    <div v-else-if="err" class="error-state">
      <span class="error-icon">⚠</span>
      <p>Xatolik yuz berdi: {{ err }}</p>
    </div>

    <div v-else class="users-grid">
      <div
        v-for="(user, index) in users"
        :key="user.id"
        class="user-card"
        :style="{ animationDelay: `${index * 0.07}s` }"
        @click="goToChat(user)"
      >
        <div class="avatar">
          <span>{{ getInitials(user.username) }}</span>
          <div class="avatar-ring"></div>
        </div>

        <div class="user-info">
          <h3 class="username">{{ user.username }}</h3>
          <p class="email">{{ user.email }}</p>
          <span class="user-id">#{{ user.id }}</span>
        </div>

        <div class="chat-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
          <span>Chat</span>
        </div>

        <div class="card-shine"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useFetch } from '@/Hooks/useFetch';

const router = useRouter();
const { getData, data: users, loading, err } = useFetch();

onMounted(() => {
  getData('/auth/users/');
});

function getInitials(name) {
  if (!name) return '?';
  return name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
}

function goToChat(user) {
//   router.push({ name: 'chat', params: { userId: user.id }, state: { user } });
    router.push("/chats")
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

.users-page {
  font-family: 'Sora', sans-serif;
  min-height: 100vh;
  background: #080b14;
  color: #e8eaf6;
  padding: 48px 24px;
  position: relative;
  overflow-x: hidden;
}

.page-header {
  text-align: center;
  margin-bottom: 56px;
  position: relative;
}

.header-glow {
  position: absolute;
  top: -60px;
  left: 50%;
  transform: translateX(-50%);
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, rgba(99,102,241,0.18) 0%, transparent 70%);
  pointer-events: none;
}

.title {
  font-size: 2.6rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #a5b4fc, #818cf8, #6366f1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #6b7280;
  font-weight: 300;
  letter-spacing: 0.04em;
}

/* Loading */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  margin-top: 80px;
  color: #6b7280;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 2px solid rgba(99,102,241,0.2);
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* Error */
.error-state {
  text-align: center;
  margin-top: 80px;
  color: #f87171;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.error-icon { font-size: 2rem; }

/* Grid */
.users-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  max-width: 1100px;
  margin: 0 auto;
}

/* Card */
.user-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 22px 24px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 18px;
  cursor: pointer;
  transition: transform 0.25s ease, border-color 0.25s ease, background 0.25s ease;
  animation: fadeUp 0.5s ease both;
  overflow: hidden;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.user-card:hover {
  transform: translateY(-4px);
  border-color: rgba(99,102,241,0.4);
  background: rgba(99,102,241,0.06);
}

.user-card:hover .card-shine {
  opacity: 1;
}

.card-shine {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(165,180,252,0.6), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}

/* Avatar */
.avatar {
  position: relative;
  flex-shrink: 0;
  width: 52px;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar span {
  position: relative;
  z-index: 2;
  font-size: 1.1rem;
  font-weight: 600;
  background: linear-gradient(135deg, #a5b4fc, #6366f1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.avatar-ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(165,180,252,0.15));
  border: 1.5px solid rgba(99,102,241,0.3);
}

/* Info */
.user-info {
  flex: 1;
  min-width: 0;
}

.username {
  font-size: 1rem;
  font-weight: 600;
  color: #e0e7ff;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.email {
  font-size: 0.78rem;
  color: #6b7280;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 6px;
}

.user-id {
  font-size: 0.7rem;
  color: rgba(99,102,241,0.6);
  font-weight: 300;
}

/* Chat button */
.chat-btn {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 10px 14px;
  background: rgba(99,102,241,0.12);
  border: 1px solid rgba(99,102,241,0.25);
  border-radius: 12px;
  color: #818cf8;
  font-size: 0.7rem;
  font-weight: 600;
  transition: all 0.2s;
  letter-spacing: 0.05em;
}

.chat-btn svg {
  width: 20px;
  height: 20px;
}

.user-card:hover .chat-btn {
  background: rgba(99,102,241,0.25);
  border-color: rgba(99,102,241,0.5);
  color: #a5b4fc;
}
</style>
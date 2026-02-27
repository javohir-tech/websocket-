<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = computed(() => localStorage.getItem('username') || 'Foydalanuvchi')

function goToChats() {
  router.push('/users')
}
</script>

<template>
  <main class="home">
    <div class="hero">
      <div class="badge">🟢 Real-time chat</div>

      <h1 class="hero-title">
        Salom, <span class="highlight">{{ username }}</span> 👋
      </h1>

      <p class="hero-desc">
        Do'stlaringiz bilan real vaqtda muloqot qiling.<br />
        Tez, qulay va xavfsiz.
      </p>

      <button class="cta-btn" @click="goToChats">
        Chatni boshlash
        <span class="arrow">→</span>
      </button>
    </div>

    <!-- Dekorativ karta -->
    <div class="preview-card">
      <div class="msg msg-left">
        <div class="avatar">A</div>
        <div class="bubble">Salom! Qalaysan? 👋</div>
      </div>
      <div class="msg msg-right">
        <div class="bubble">Yaxshi, sen-chi? 😄</div>
        <div class="avatar self">S</div>
      </div>
      <div class="msg msg-left">
        <div class="avatar">A</div>
        <div class="bubble">Kecha film ko'rdim, ajoyib edi!</div>
      </div>
      <div class="msg msg-right">
        <div class="bubble">Qaysi film? 🎬</div>
        <div class="avatar self">S</div>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

.home {
  font-family: 'Sora', sans-serif;
  min-height: calc(100vh - 60px);
  background: #0d0d0d;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 1.5rem;
}

/* Hero */
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1.2rem;
}

.badge {
  font-size: 0.78rem;
  font-weight: 500;
  color: #888;
  background: #141414;
  border: 1px solid #222;
  border-radius: 20px;
  padding: 0.35rem 0.9rem;
  letter-spacing: 0.3px;
}

.hero-title {
  font-size: clamp(2rem, 6vw, 3.2rem);
  font-weight: 700;
  color: #fff;
  letter-spacing: -1px;
  line-height: 1.15;
}

.highlight {
  color: #e8ff47;
}

.hero-desc {
  font-size: 1rem;
  color: #555;
  line-height: 1.7;
}

.cta-btn {
  font-family: 'Sora', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: #0d0d0d;
  background: #e8ff47;
  border: none;
  border-radius: 10px;
  padding: 0.75rem 1.8rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  transition: opacity 0.2s, transform 0.15s;
}

.cta-btn:hover {
  opacity: 0.88;
  transform: translateY(-2px);
}

.arrow {
  font-size: 1.1rem;
  transition: transform 0.2s;
}

.cta-btn:hover .arrow {
  transform: translateX(4px);
}

/* Preview Card */
.preview-card {
  width: 100%;
  max-width: 360px;
  background: #111;
  border: 1px solid #1f1f1f;
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.msg {
  display: flex;
  align-items: flex-end;
  gap: 0.6rem;
}

.msg-right {
  flex-direction: row-reverse;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1e1e1e;
  border: 1px solid #2a2a2a;
  color: #888;
  font-size: 0.75rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.avatar.self {
  background: #1e2a00;
  border-color: #3a5200;
  color: #e8ff47;
}

.bubble {
  font-size: 0.85rem;
  color: #ccc;
  background: #171717;
  border: 1px solid #1f1f1f;
  border-radius: 12px;
  padding: 0.55rem 0.9rem;
  max-width: 240px;
  line-height: 1.5;
}

.msg-right .bubble {
  background: #1a2600;
  border-color: #2a3d00;
  color: #e8ff47;
}

@media (max-width: 480px) {
  .preview-card {
    max-width: 100%;
  }
}
</style>
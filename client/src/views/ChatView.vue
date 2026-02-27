<template>
  <div class="chat-wrap">
    <div class="chat-header">
      <span class="chat-dot"></span>
      <span class="chat-title">general</span>
      <span class="chat-subtitle">jonli kanal</span>
    </div>

    <div class="chat-body" ref="bodyRef">
      <transition-group name="msg" tag="div">
        <div v-for="(msg, i) in messages" :key="i" class="msg-row" :class="{ 'msg-row--own': msg.author === 'me' }">
          <div class="msg-avatar">{{ msg.author?.[0]?.toUpperCase() ?? '?' }}</div>
          <div class="msg-bubble">
            <span class="msg-author">{{ msg.author }}</span>
            <p class="msg-text">{{ msg.message }}</p>
          </div>
        </div>
      </transition-group>
    </div>

    <div class="chat-footer">
      <input v-model="newMessage" @keyup.enter="send" placeholder="Xabar yoz..." class="chat-input" />
      <button @click="send" class="chat-send" :disabled="!newMessage.trim()">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
          stroke-linecap="round" stroke-linejoin="round">
          <line x1="22" y1="2" x2="11" y2="13" />
          <polygon points="22 2 15 22 11 13 2 9 22 2" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useChat } from '@/composables/useChat'
import { useRoute } from 'vue-router'

const route = useRoute()
const { messages, connect, sendMessage, disconnect } = useChat(route.params.userId)  // ✅ messages
const newMessage = ref('')
const bodyRef = ref(null)

// O'zingizning ID'ingizni saqlang (token'dan yoki store'dan)
const myId = localStorage.getItem('user_id')  // yoki Pinia store

function send() {
  if (newMessage.value.trim()) {
    sendMessage(newMessage.value)
    newMessage.value = ''
  }
}

function scrollToBottom() {
  nextTick(() => {
    if (bodyRef.value) bodyRef.value.scrollTop = bodyRef.value.scrollHeight
  })
}

watch(messages, scrollToBottom, { deep: true })

onMounted(() => {
  connect()
  scrollToBottom()
})
onUnmounted(() => disconnect())
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@600;700&display=swap');

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chat-wrap {
  --bg: #0d0d10;
  --surface: #16161c;
  --border: #2a2a35;
  --accent: #c8f135;
  --accent-dim: #9ab82a;
  --text: #e8e8f0;
  --muted: #6b6b80;
  --bubble-bg: #1e1e28;
  --bubble-own: #252e10;
  --radius: 16px;
  --font-mono: 'DM Mono', monospace;
  --font-head: 'Syne', sans-serif;

  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 520px;
  height: 640px;
  margin: 0 auto;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  font-family: var(--font-mono);
  box-shadow: 0 0 0 1px #ffffff06, 0 32px 80px #000000cc;
}

/* ─── HEADER ─────────────────────────────── */
.chat-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

.chat-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 10px var(--accent);
  animation: pulse 2s ease-in-out infinite;
  flex-shrink: 0;
}

@keyframes pulse {

  0%,
  100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.8);
  }
}

.chat-title {
  font-family: var(--font-head);
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 0.04em;
}

.chat-subtitle {
  font-size: 11px;
  color: var(--muted);
  margin-left: auto;
  letter-spacing: 0.08em;
  text-transform: lowercase;
}

/* ─── BODY ────────────────────────────────── */
.chat-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scrollbar-width: thin;
  scrollbar-color: var(--border) transparent;
}

.chat-body::-webkit-scrollbar {
  width: 4px;
}

.chat-body::-webkit-scrollbar-track {
  background: transparent;
}

.chat-body::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 4px;
}

/* ─── MESSAGE ROW ─────────────────────────── */
.msg-row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  max-width: 82%;
}

.msg-row--own {
  flex-direction: row-reverse;
  align-self: flex-end;
}

.msg-avatar {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--border);
  color: var(--text);
  font-size: 12px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid #ffffff10;
}

.msg-row--own .msg-avatar {
  background: var(--bubble-own);
  border-color: var(--accent-dim);
  color: var(--accent);
}

.msg-bubble {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.msg-author {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 0.06em;
  padding-left: 2px;
}

.msg-row--own .msg-author {
  text-align: right;
  padding-left: 0;
  padding-right: 2px;
}

.msg-text {
  background: var(--bubble-bg);
  color: var(--text);
  font-size: 13.5px;
  line-height: 1.55;
  padding: 10px 14px;
  border-radius: 12px 12px 12px 4px;
  border: 1px solid var(--border);
  word-break: break-word;
}

.msg-row--own .msg-text {
  background: var(--bubble-own);
  border-color: #3a4a10;
  border-radius: 12px 12px 4px 12px;
  color: #d8f080;
}

/* ─── FOOTER ──────────────────────────────── */
.chat-footer {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-top: 1px solid var(--border);
  background: var(--surface);
  flex-shrink: 0;
}

.chat-input {
  flex: 1;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 14px;
  color: var(--text);
  font-family: var(--font-mono);
  font-size: 13px;
  outline: none;
  transition: border-color 0.2s;
  caret-color: var(--accent);
}

.chat-input::placeholder {
  color: var(--muted);
}

.chat-input:focus {
  border-color: var(--accent-dim);
  box-shadow: 0 0 0 2px #c8f13515;
}

.chat-send {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--accent);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background 0.15s, transform 0.12s, opacity 0.15s;
  color: #111;
}

.chat-send svg {
  width: 16px;
  height: 16px;
}

.chat-send:hover:not(:disabled) {
  background: #d6ff45;
  transform: scale(1.06);
}

.chat-send:active:not(:disabled) {
  transform: scale(0.95);
}

.chat-send:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

/* ─── TRANSITIONS ─────────────────────────── */
.msg-enter-active {
  transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.msg-enter-from {
  opacity: 0;
  transform: translateY(14px) scale(0.96);
}
</style>
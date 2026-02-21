<template>
  <nav class="navbar" :class="{ 'menu-open': isMenuOpen }">
    <div class="navbar-container">
      <!-- Logo -->
      <RouterLink to="/" class="navbar-logo" @click="closeMenu">
        <span class="logo-icon">⬡</span>
        <span class="logo-text">MyApp</span>
      </RouterLink>

      <!-- Desktop Links -->
      <div class="navbar-links desktop-links">
        <RouterLink to="/" class="nav-link" exact-active-class="active">
          <span class="link-icon">🏠</span>
          <span>Home</span>
        </RouterLink>
        <RouterLink to="/chat" class="nav-link" active-class="active">
          <span class="link-icon">💬</span>
          <span>Chat</span>
        </RouterLink>
      </div>

      <!-- Desktop Logout -->
      <div class="navbar-actions desktop-links">
        <button class="logout-btn" @click="handleLogout">
          <span>Logout</span>
          <span class="logout-icon">→</span>
        </button>
      </div>

      <!-- Hamburger -->
      <button class="hamburger" @click="toggleMenu" :aria-expanded="isMenuOpen" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>

    <!-- Mobile Menu -->
    <div class="mobile-menu" :class="{ open: isMenuOpen }">
      <RouterLink to="/" class="nav-link" exact-active-class="active" @click="closeMenu">
        <span class="link-icon">🏠</span>
        <span>Home</span>
      </RouterLink>
      <RouterLink to="/chat" class="nav-link" active-class="active" @click="closeMenu">
        <span class="link-icon">💬</span>
        <span>Chat</span>
      </RouterLink>
      <button class="logout-btn" @click="handleLogout">
        <span>Logout</span>
        <span class="logout-icon">→</span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleLogout = () => {
  closeMenu()
  // O'z logout logikangizni shu yerga qo'shing
  // Masalan: authStore.logout()
  console.log('Logged out')
  router.push('/')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@600;700&display=swap');

*,
*::before,
*::after {
  box-sizing: border-box;
}

.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: #0a0a0f;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  font-family: 'DM Mono', monospace;
  backdrop-filter: blur(12px);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 64px;
  display: flex;
  align-items: center;
  gap: 2rem;
}

/* Logo */
.navbar-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-icon {
  font-size: 1.4rem;
  color: #7c6aff;
  line-height: 1;
}

.logo-text {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: 1.1rem;
  color: #ffffff;
  letter-spacing: -0.02em;
}

/* Links */
.navbar-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  flex: 1;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 0.9rem;
  border-radius: 8px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.55);
  font-size: 0.85rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  transition: color 0.2s, background 0.2s;
}

.nav-link:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.06);
}

.nav-link.active {
  color: #7c6aff;
  background: rgba(124, 106, 255, 0.12);
}

.link-icon {
  font-size: 0.9rem;
}

/* Actions */
.navbar-actions {
  margin-left: auto;
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 1rem;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'DM Mono', monospace;
  font-size: 0.82rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  letter-spacing: 0.01em;
}

.logout-btn:hover {
  border-color: #ff6a6a;
  color: #ff6a6a;
  background: rgba(255, 106, 106, 0.08);
}

.logout-icon {
  transition: transform 0.2s;
}

.logout-btn:hover .logout-icon {
  transform: translateX(3px);
}

/* Hamburger */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: 6px;
  background: none;
  border: none;
  cursor: pointer;
  margin-left: auto;
}

.hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 2px;
  transition: transform 0.25s, opacity 0.25s;
  transform-origin: center;
}

.menu-open .hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.menu-open .hamburger span:nth-child(2) {
  opacity: 0;
}
.menu-open .hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

/* Mobile Menu */
.mobile-menu {
  display: none;
  flex-direction: column;
  padding: 0.75rem 1.5rem 1rem;
  gap: 0.25rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  background: #0a0a0f;
}

.mobile-menu .logout-btn {
  margin-top: 0.5rem;
  width: fit-content;
}

/* Responsive */
@media (max-width: 640px) {
  .desktop-links {
    display: none !important;
  }

  .hamburger {
    display: flex;
  }

  .mobile-menu.open {
    display: flex;
  }
}
</style>
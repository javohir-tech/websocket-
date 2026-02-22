<template>
  <nav class="navbar">
    <div class="nav-inner">
      <!-- Logo -->
      <RouterLink to="/" class="nav-logo">⬡ App</RouterLink>

      <!-- Nav Links -->
      <div class="nav-links">
        <RouterLink to="/" class="nav-link">Home</RouterLink>
        <RouterLink to="/chats" class="nav-link">Chats</RouterLink>
      </div>

      <!-- Auth Buttons -->
      <div class="nav-auth">
        <template v-if="isLoggedIn">
          <button class="btn btn-logout" @click="handleLogOut">Log Out</button>
        </template>
        <template v-else>
          <RouterLink to="/singup" class="btn btn-outline">Sign Up</RouterLink>
          <RouterLink to="/singin" class="btn btn-primary">Sign In</RouterLink>
        </template>
      </div>

      <!-- Mobile Hamburger -->
      <button class="burger" @click="menuOpen = !menuOpen" aria-label="Menu">
        <span :class="{ open: menuOpen }"></span>
        <span :class="{ open: menuOpen }"></span>
        <span :class="{ open: menuOpen }"></span>
      </button>
    </div>

    <!-- Mobile Menu -->
    <div class="mobile-menu" :class="{ active: menuOpen }">
      <RouterLink to="/" class="nav-link" @click="menuOpen = false">Home</RouterLink>
      <RouterLink to="/chats" class="nav-link" @click="menuOpen = false">Chats</RouterLink>
      <template v-if="isLoggedIn">
        <button class="btn btn-logout" @click="handleLogOut">Log Out</button>
      </template>
      <template v-else>
        <RouterLink to="/singup" class="btn btn-outline" @click="menuOpen = false">Sign Up</RouterLink>
        <RouterLink to="/singin" class="btn btn-primary" @click="menuOpen = false">Sign In</RouterLink>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const menuOpen = ref(false)

const isLoggedIn = computed(() => !!localStorage.getItem('accessToken'))

function handleLogOut() {
  localStorage.removeItem('accessToken')
  menuOpen.value = false
  router.push('/signin')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600&display=swap');

.navbar {
  font-family: 'Sora', sans-serif;
  position: sticky;
  top: 0;
  z-index: 100;
  background: #0d0d0d;
  border-bottom: 1px solid #1f1f1f;
}

.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 60px;
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-logo {
  font-size: 1.2rem;
  font-weight: 600;
  color: #e8ff47;
  text-decoration: none;
  letter-spacing: -0.5px;
  flex-shrink: 0;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  flex: 1;
}

.nav-link {
  color: #888;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  transition: color 0.2s, background 0.2s;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #fff;
  background: #1a1a1a;
}

.nav-auth {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-left: auto;
}

.btn {
  font-family: 'Sora', sans-serif;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.4rem 1rem;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: opacity 0.2s, transform 0.15s;
  display: inline-flex;
  align-items: center;
}

.btn:hover {
  opacity: 0.85;
  transform: translateY(-1px);
}

.btn-primary {
  background: #e8ff47;
  color: #0d0d0d;
}

.btn-outline {
  background: transparent;
  color: #ccc;
  border: 1px solid #333;
}

.btn-outline:hover {
  border-color: #666;
  color: #fff;
}

.btn-logout {
  background: transparent;
  color: #ff5f5f;
  border: 1px solid #3a1a1a;
}

.btn-logout:hover {
  background: #1f0a0a;
}

/* Burger */
.burger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  margin-left: auto;
}

.burger span {
  display: block;
  width: 22px;
  height: 2px;
  background: #ccc;
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

.burger span.open:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.burger span.open:nth-child(2) { opacity: 0; }
.burger span.open:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* Mobile Menu */
.mobile-menu {
  display: none;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem 1.5rem;
  border-top: 1px solid #1a1a1a;
  background: #0d0d0d;
}

.mobile-menu.active {
  display: flex;
}

@media (max-width: 640px) {
  .nav-links,
  .nav-auth {
    display: none;
  }

  .burger {
    display: flex;
  }

  .mobile-menu .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
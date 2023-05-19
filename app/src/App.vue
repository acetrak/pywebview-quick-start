<script setup>

</script>

<template>
  <v-app>
    <router-view v-slot="{ Component, route }">
      <transition :name="route.meta?.transition || 'slide-fade'" mode="out-in">
        <component :is="Component"/>
      </transition>
    </router-view>
  </v-app>
</template>

<style lang="scss">
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s ease-out;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>

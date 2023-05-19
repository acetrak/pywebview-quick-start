
<script setup>
import {useTheme} from 'vuetify'
import {useRouter} from "vue-router";

const router = useRouter()

const theme = useTheme()

const toggleTheme = () => theme.global.name.value = theme.global.current.value.dark ? 'myCustomLightTheme' : 'dark'

</script>

<template>
<div>
  home
  <v-container>
      <v-btn variant="elevated" prepend-icon="mdi-vuetify" @click="toggleTheme">toggle theme</v-btn>

      <v-btn
          block
          class="text-none mb-4"
          color="primary"
          variant="elevated"
          @click="router.push('/about')"
      >
        Verify and continue
      </v-btn>

    </v-container>

</div>
</template>


<style scoped>

</style>
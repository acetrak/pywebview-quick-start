<script setup>
import {useRouter} from "vue-router";

const router = useRouter()
</script>


<template>
  <div>
    about
    <v-btn
        block
        class="text-none mb-4"
        color="primary"
        variant="elevated"
        @click="router.push('/')"
    >
      Verify and continue
    </v-btn>

  </div>
</template>



<style scoped>

</style>
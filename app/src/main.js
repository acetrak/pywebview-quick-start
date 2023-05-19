import {createApp} from 'vue'
import './style.scss'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import vueRouter from '@/plugins/vue-router'

// Vuetify
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

const app = createApp(App)

app.use(vuetify)
app.use(vueRouter)

app.mount('#app')

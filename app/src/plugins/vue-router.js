import * as VueRouter from 'vue-router'

const routes = [
    {path: '/', component: () => import('@/pages/home/index.vue')},
    {path: '/about', component: () => import('@/pages/about/index.vue')},
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

export default router
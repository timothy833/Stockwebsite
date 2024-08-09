import { createRouter, createWebHistory,  } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'


const routes:Array<RouteRecordRaw> = [
    {
        path:"/",
        name:"Home",
        component:()=> import('.')
    },
    {
        path:"/stockindex",
        name:"stockindex",
        component:()=> import('../components/stockindex.vue')
    },
    // {   path:"/stock2",
    //     name:"0050",
    //     component:()=> import('../components/stock2.vue')
    // }
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
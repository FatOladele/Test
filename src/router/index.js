import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import test from '../views/test.vue'
import wroom from '../views/wroom.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/play',
    name: 'play',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/play.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: test
  },
  {
    path: '/game',
    name: 'game',
    component: wroom
  }
]

const router = new VueRouter({
  routes
})

export default router

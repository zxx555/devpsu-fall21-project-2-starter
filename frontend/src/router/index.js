import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ToDoList from '../views/ToDoList.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/todolist',
      name: 'todolist',
      component: ToDoList
    },
    {
      path: '*',
      redirect: '/'
    }
  ],
  linkActiveClass: 'active',
})

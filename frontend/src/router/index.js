import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ToDoList from '../views/ToDoList.vue'
import ShoppingList from '../views/ShoppingList.vue'

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
		path: '/shoppinglist',
		name: 'shoppinglist',
		component: ShoppingList
	},
    {
      path: '*',
      redirect: '/'
    }
  ],
  linkActiveClass: 'active',
})

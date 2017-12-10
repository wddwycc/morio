import Home from './Home.vue';
import Login from './Login.vue';
import Register from './Register.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register,
  },
];

export default {
  routes,
  mode: 'history',
}

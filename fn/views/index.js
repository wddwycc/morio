import Home from './Home.vue';
import Login from './Login.vue';
import Register from './Register.vue';
import Repository from './Repository.vue';


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
  {
    path: '/user/:name/:repo_id',
    name: 'repository',
    component: Repository,
  },
];

export default {
  routes,
  mode: 'history',
}

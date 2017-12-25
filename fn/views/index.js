import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Repo from './Repo.vue'
import NewRepo from './NewRepo.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  // user
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  // core
  {
    path: '/new',
    name: 'NewRepo',
    component: NewRepo,
  },
  {
    path: '/user/:name/:repo_id',
    name: 'Repo',
    component: Repo,
  },
];

export default {
  routes,
  mode: 'history',
}

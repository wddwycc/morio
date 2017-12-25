import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Repo from './Repo.vue'
import NewRepo from './NewRepo.vue'
import User from './User.vue'


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
    path: '/user/:username',
    name: 'User',
    component: User,
  },
  {
    path: '/user/:username/:repo_name',
    name: 'Repo',
    component: Repo,
  },
];

export default {
  routes,
  mode: 'history',
}

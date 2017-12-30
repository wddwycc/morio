import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Repo from './Repo/index.vue'
import RepoCards from './Repo/Cards.vue'
import RepoSetting from './Repo/Setting.vue'
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
    component: Repo,
    children: [
      {
        path: '',
        name: 'Repo',
        component: RepoCards,
      },
      {
        path: 'setting',
        name: 'RepoSetting',
        component: RepoSetting,
      },
    ],
  },
];

export default {
  routes,
  mode: 'history',
}

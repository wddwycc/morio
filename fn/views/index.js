import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Confirm from './Confirm.vue'
import Repo from './Repo/index.vue'
import RepoCards from './Repo/Cards.vue'
import RepoSetting from './Repo/Setting.vue'
import NewRepo from './NewRepo.vue'
import User from './User.vue'
import Course from './Course.vue'


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
  {
    path: '/confirm',
    name: 'Confirm',
    component: Confirm,
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
  {
    path: '/course/:id',
    name: 'Course',
    component: Course,
  },
];

export default {
  routes,
  mode: 'history',
}

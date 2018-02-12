import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import Confirm from './Confirm.vue'
import NewRepo from './NewRepo.vue'
import Repo from './Repo.vue'
import User from './User.vue'
import NewCourse from './NewCourse.vue'
import Course from './Course.vue'
import NotFound from './404.vue'


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
    path: '/new-repo',
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
  {
    path: '/new-course',
    name: 'NewCourse',
    component: NewCourse,
  },
  {
    path: '/course/:id',
    name: 'Course',
    component: Course,
  },
  { path: '*', component: NotFound }
];

export default {
  routes,
  mode: 'history',
}

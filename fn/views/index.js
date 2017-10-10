import Home from './Home.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
];

export default {
  routes,
  mode: 'history',
}

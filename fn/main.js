import './css/normalize.css'

import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import { Button, Menu, MenuItem } from 'element-ui'

import routerConfig from './views/index'

Vue.use(VueRouter)

Vue.use(Button)
Vue.use(Menu)
Vue.use(MenuItem)

const router = new VueRouter(routerConfig);

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({ router });
  app.$mount(rootEl);
}

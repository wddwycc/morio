import './css/normalize.css'
import './css/variable.css'

import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import {
  Button,
  Form,
  FormItem,
  Input,
  Menu,
  MenuItem,
} from 'element-ui'
import routerConfig from './views/index'
import store from './store/index';

Vue.use(VueRouter)

Vue.use(Button)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Input)
Vue.use(Form)
Vue.use(FormItem)

const router = new VueRouter(routerConfig);

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({router, store});
  app.$mount(rootEl);
}

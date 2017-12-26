import './css/normalize.css'
import './css/variable.css'
import './css/base.css'
import './css/vendor.css'

import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import {
  Button, Card, Form, FormItem, Input, Menu, MenuItem,
  Switch, Row, Col,
} from 'element-ui'
import routerConfig from './views/index'
import store from './store/index';
import components from './components/index'

Vue.use(VueRouter)
Vue.use(components)

Vue.use(Button)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Input)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Card)
Vue.use(Switch)
Vue.use(Row)
Vue.use(Col)

const router = new VueRouter(routerConfig);

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({router, store});
  app.$mount(rootEl);
}

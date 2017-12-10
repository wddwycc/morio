import './css/normalize.css'

import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import App from './App.vue'

import {
  Button,
  Form,
  FormItem,
  Input,
  Menu,
  MenuItem,
  Message,
} from 'element-ui'
import routerConfig from './views/index'
import store from './store/index';

Vue.use(VueRouter)
Vue.use(VueResource)

Vue.use(Button)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Input)
Vue.use(Form)
Vue.use(FormItem)

const router = new VueRouter(routerConfig);

Vue.http.interceptors.push(function (request, next) {
  const authToken = store.state.user.authToken
  if (authToken) {
    request.headers.set('Authorization', authToken)
  }
  next((res) => {
    if (res.ok) {
      return
    }
    let msg = res.statusText
    if (res.body.hasOwnProperty('error')) {
      msg = res.body['error']
    }
    Message.error(msg)
  })
});

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({router, store});
  app.$mount(rootEl);
}

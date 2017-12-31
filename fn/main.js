import './css/normalize.css'
import './css/variable.css'
import './css/base.css'
import './css/vendor.css'

import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import {
  Button, Card, Col, Dropdown, DropdownItem, DropdownMenu, Form,
  FormItem, Input, Menu, MenuItem, Row, Switch, TabPane, Tabs,
  Dialog, MessageBox
} from 'element-ui'
import routerConfig from './views/index'
import store from './store/index';
import components from './components/index'
import VueTimeago from 'vue-timeago'

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
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(TabPane)
Vue.use(Tabs)
Vue.use(Dialog)

const MsgBox = MessageBox;
Vue.prototype.$confirm = MsgBox.confirm

Vue.use(VueTimeago, {
  locale: 'en-US',
  locales: {
    'en-US': require('vue-timeago/locales/en-US.json'),
  }
})

const router = new VueRouter(routerConfig);

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({router, store});
  app.$mount(rootEl);
}

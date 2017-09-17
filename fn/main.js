require('./css/normalize.css')

import Vue from 'vue'
import App from './App.vue'

const rootEl = document.getElementById('app');
if (rootEl) {
  const RootApp = Vue.extend(App);
  const app = new RootApp({});
  app.$mount(rootEl);
}



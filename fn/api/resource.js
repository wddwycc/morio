import Vue from 'vue'
import VueResource from 'vue-resource'


Vue.use(VueResource)


export const loginResource = Vue.resource('/api/user/login')
export const registerResource = Vue.resource('/api/user/register')

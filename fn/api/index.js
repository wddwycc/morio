import axios from 'axios'
import db from '../store/db'
import {Message} from 'element-ui'

let client = axios.create({
  baseURL: '/api',
  timeout: 1000,
});

client.interceptors.request.use(request => {
  const authToken = db.get('authToken')
  if (authToken) {
    request.headers['authorization'] = authToken
  }
  return request
});

client.interceptors.response.use(response => {
  const authToken = response.headers['authorization']
  if (authToken) {
    db.set('authToken', authToken)
  }
  return response
}, error => {
  let msg = error.response.data.msg || error.response.statusText
  Message.error(msg)
  return Promise.reject(error)
});

export default {
  register: (data) => {
    return client.post('/user/register', {...data})
  },
  login: (data) => {
    return client.post('/user/login', {...data})
  },
  getRepos: () => {
    return client.get('/repos')
  },
  newRepo: (data) => {
    return client.post('/repos', {...data})
  }
}

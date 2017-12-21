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
    request.headers['Authorization'] = authToken
  }
  return request
});

client.interceptors.response.use(response => {
  const authToken = response.headers['Authorization']
  if (authToken) {
    db.set('authToken', authToken)
  }
  return response
}, error => {
  let msg = error.response.data.error || error.response.statusText
  Message.error(msg)
  return Promise.reject(error)
});

export default {
  register: (data) => {
    return client.post('/user/register', {...data})
  },
}

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
  if (error.response.status === 401) {} else {
    Message.error(msg)
  }
  return Promise.reject(error)
});

export default {
  // user
  me: () => {
    return client.get('/user/me')
  },
  register: (data) => {
    return client.post('/user/register', {...data})
  },
  login: (data) => {
    return client.post('/user/login', {...data})
  },
  // query
  getUser: (username) => {
    return client.get(`/users/${username}`)
  },
  getRepos: (username) => {
    return client.get(`/users/${username}/repos`)
  },
  getRepo: (username, repoName) => {
    return client.get(`/users/${username}/repos/${repoName}`)
  },
  updateRepo: (username, repoName, data) => {
    return client.put(`/users/${username}/repos/${repoName}`, data)
  },
  getCards: (username, repoName) => {
    return client.get(`/users/${username}/repos/${repoName}/cards`)
  },
  // updates
  newRepo: (data) => {
    return client.post('/repos', data)
  },
  newCard: (data) => {
    return client.post(`/cards`, data)
  },
  delCard: (id) => {
    return client.delete(`/cards/${id}`)
  },
}

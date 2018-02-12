import axios from 'axios'
import db from '../store/db'
import {Message} from 'element-ui'

let client = axios.create({
  baseURL: '/api',
  timeout: 10000,
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
  if (!error.response) {
    Message.error(error.message)
  } else {
    let msg = error.response.data.msg || error.response.statusText
    if (error.response.status === 401) {
    } else if (error.response.status === 403) {
      db.del('authToken')
      Message.error(msg)
    } else {
      Message.error(msg)
    }
  }
  return Promise.reject(error)
});

export default {
  // account related
  me: () => {
    return client.get('/user/me')
  },
  register: (data) => {
    return client.post('/user/register', {...data})
  },
  login: (data) => {
    return client.post('/user/login', {...data})
  },
  confirm: (token) => {
    return client.post('/user/confirm', {token: token})
  },
  // query
  getUser: (username) => {
    return client.get(`/users/${username}`)
  },
  getUserRepos: (username) => {
    return client.get(`/users/${username}/repos`)
  },
  getRepo: (username, repoName) => {
    return client.get(`/users/${username}/repos/${repoName}`)
  },
  getRepoById: (id) => {
    return client.get(`/repos/${id}`)
  },
  getCards: (username, repoName, params) => {
    return client.get(`/users/${username}/repos/${repoName}/cards`, {params: params})
  },
  // my
  myRepos: () => {
    return client.get('/repos')
  },
  newRepo: (data) => {
    return client.post('/repos', data)
  },
  updateRepo: (repo_id, data) => {
    return client.put(`/repos/${repo_id}`, data)
  },

  newCard: (data) => {
    return client.post(`/cards`, data)
  },
  delCard: (id) => {
    return client.delete(`/cards/${id}`)
  },

  myCourses: () => {
    return client.get('/courses')
  },
  newCourse: (data) => {
    return client.post('/courses', data)
  },
  getCourseById: (id) => {
    return client.get(`/courses/${id}`)
  },
  delCourse: (id) => {
    return client.delete(`/courses/${id}`)
  },
  courseNextCard: (course_id, data) => {
    return client.post(`/courses/${course_id}/next`, data)
  },
}

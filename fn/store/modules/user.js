import db from '../db'


const UPDATE_AUTO_TOKEN = 'UPDATE_AUTO_TOKEN'


const state = {
  authToken: db.get('authToken') || null,
}

const mutations = {
  [UPDATE_AUTO_TOKEN](state, authToken) {
    state.authToken = authToken
    db.set('authToken', authToken)
  }
}

const actions = {
  updateAuthToken({commit}, token) {
    commit(UPDATE_AUTO_TOKEN, token)
  }
}

export default {
  state,
  mutations,
  actions,
}

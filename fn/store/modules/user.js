const state = {
  loading: true,
  name: null,
  avatar: null,
}

const mutations = {
  loadUser(state, data) {
    state.loading = false
    if (data) {
      state.name = data.name
      state.avatar = data.avatar
    }
  },
  dropUser(state) {
    state.name = null
    state.avatar = null
  },
}

const actions = {
}

export default {
  state,
  mutations,
  actions,
}

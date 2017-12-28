const state = {
  loading: true,
  name: null,
}

const mutations = {
  loadUser(state, data) {
    state.loading = false
    if (data) {
      state.name = data.name
    }
  },
  dropUser(state) {
    state.name = null
  },
}

const actions = {
}

export default {
  state,
  mutations,
  actions,
}

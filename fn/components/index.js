import RepoCell from './RepoCell.vue'
import Empty from './Empty.vue'


function install(Vue) {
  Vue.component(RepoCell.name, RepoCell)
  Vue.component(Empty.name, Empty)
}

export default { install }

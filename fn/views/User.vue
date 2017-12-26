<template>
  <div>
    <h1>{{ username }}</h1>

    <div>
      <repo-cell></repo-cell>
      <el-card class="repo-cell" v-for="repo in repos" :key="repo.id">
        <div slot="header" class="repo-cell__name">
          <router-link :to="{ name: 'Repo', params: { username: repo.username, repo_name: repo.name, repoId: repo.id }}" tag="div"> {{ repo.name }}</router-link>
        </div>
        <div>
          <span class="repo-cell__date"> {{ repo['updated_at'] }} </span>
          <span class="repo-cell__desc"> {{ repo.desc }}</span>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  import api from '../api'

  export default {
    data() {
      return {
        repos: [],
      }
    },
    computed: {
      username: function() {
        return this.$route.params['username']
      }
    },
    methods: {
      fetchRepos() {
        api.getRepos(this.username).then((resp) => {
          this.repos = resp.data
        })
      }
    },
    mounted: function () {
      this.fetchRepos()
    },
  }
</script>

<style scoped>

</style>
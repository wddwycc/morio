<template>
  <div>
    <h1>{{ this.$route.params['username'] }}</h1>

    <div>
      <el-card class="repo-cell" v-for="repo in repos" :key="repo.id">
        <div slot="header" class="repo-cell__name">
          <router-link :to="{ name: 'Repo', params: { username: repo.username, repo_name: repo.name }}" tag="div"> {{ repo.name }}</router-link>
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
    methods: {
      fetchRepos() {
        api.getRepos().then((resp) => {
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
<template>
  <div>
    <div class="repositories">
      <el-card class="repository" v-for="repo in repos" :key="repo.id">
        <div slot="header" class="repository__name">
          <router-link :to="{ name: 'Repo', params: { username: repo.username, repo_name: repo.name }}" tag="div"> {{ repo.name }}</router-link>
        </div>
        <div>
          <span class="repository__date"> {{ repo['updated_at'] }} </span>
          <span class="repository__desc"> {{ repo.desc }}</span>
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
    mounted: function() {
      this.fetchRepos()
    }
  }
</script>

<style>
  .repository {
    margin-bottom: 18px;
  }

  .repository__name {
  }

  .repository__date {
    color: var(--color-grey);
    font-size: var(--size-x-small);
  }

  .repository__desc {
    margin-left: 18px;
    color: var(--color-light-grey);
  }
</style>

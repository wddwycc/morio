<template>
  <div>
    <div class="repositories">
      <el-card class="repository" v-for="repo in repos" :key="repo.id">
        <div slot="header" class="repository__name">
          <router-link :to = "{ name: 'Repo', params: { name: 'name', repo_id: repo.name }}"> {{ repo.name }} </router-link>
        </div>
        <div>
          <span class="repository__date"> {{ repo.date }} </span>
          <span class="repository__desc"> {{ repo.desc }}</span>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        repos: [
          {
            id: 1,
            name: '英语',
            date: '20171201',
            desc: '英语单词'
          },
          {
            id: 2,
            name: '日语',
            date: '20171214',
            desc: '日语单词'
          },
        ]
      }
    },
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

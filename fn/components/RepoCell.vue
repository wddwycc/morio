<template>
  <div>
    <el-card class="repo-cell">
      <div slot="header" class="repo-cell__name">
        <router-link :to="{ name: 'Repo', params: { username: data.username, repo_name: data.name, repoId: data.id }}" tag="div"> {{ data.name }}</router-link>
      </div>
      <div>
        <span class="repo-cell__date"> {{ data.updated_at }} </span>
        <span class="repo-cell__desc"> {{ data.desc }}</span>
      </div>
    </el-card>
  </div>
</template>

<script>


  export default {
    name: "repo-cell",
    props: ['data'],
  }
</script>

<style scoped>

</style>
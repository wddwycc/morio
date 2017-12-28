<template>
  <div>
    <el-card class="repo-cell">
      <div slot="header" class="repo-cell__name">
        <router-link :to="{ name: 'Repo', params: { username: data.username, repo_name: data.name, repoId: data.id }}" tag="div"> {{ data.name }}</router-link>
      </div>
      <div>
        <timeago :since="data['updated_at']" :auto-update="60"></timeago>
        <span class="repo-cell__desc"> {{ data['desc'] }}</span>
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

<style>
  .repo-cell {
    margin-bottom: 18px;
  }

  .repo-cell__name {
  }

  .repo-cell__date {
    color: var(--color-grey);
    font-size: var(--size-x-small);
  }

  .repo-cell__desc {
    margin-left: 18px;
    color: var(--color-light-grey);
  }
</style>
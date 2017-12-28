<template>
  <div>
    <el-card class="repo-cell">
      <div slot="header" class="repo-cell__header">
        <router-link :to="{ name: 'Repo', params: { username: data.username, repo_name: data.name, repoId: data.id }}" tag="div">
          <el-button type="text">{{ data.name }}</el-button>
        </router-link>
      </div>
      <div>
        <div class="repo-cell__desc"> {{ data['desc'] || 'No detail abount the repository' }}</div>
        <div class="repo-cell__date"><span>Updated </span>
          <timeago :since="data['updated_at']" :auto-update="60"></timeago>
        </div>
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

  .repo-cell__header .el-button {
    padding: 0;
    font-size: var(--size-medium);
  }

  .repo-cell__desc {
    font-size: var(--size-small);
    margin-bottom: 20px;
  }

  .repo-cell__date {
    color: var(--color-light-grey);
    font-size: var(--size-xx-small);
  }
</style>
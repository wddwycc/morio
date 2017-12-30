<template>
  <div>
    <repo-cell v-for="repo in stars" :data="repo" :key="repo.id"></repo-cell>
  </div>
</template>

<script>
  export default {
    props: ['stars']
  }
</script>

<style scoped>

</style>
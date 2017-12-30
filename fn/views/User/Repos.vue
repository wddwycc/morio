<template>
  <div>
    <repo-cell v-for="repo in repos" :data="repo" :key="repo.id"></repo-cell>
  </div>
</template>

<script>
  export default {
    props: ['repos']
  }
</script>

<style scoped>

</style>
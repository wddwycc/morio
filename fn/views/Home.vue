<template>
  <div>
    <!--  todo: replace with landing page -->
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
      // this.fetchRepos()
    }
  }
</script>

<style>
</style>

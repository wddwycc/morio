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

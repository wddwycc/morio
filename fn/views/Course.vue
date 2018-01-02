<template>
  <div>

  </div>
</template>

<script>
  import api from '../api'

  export default {
    data() {
      return {
        repo: {},
        card: null,
      }
    },
    mounted() {
      api.courseNextCard(this.$route.params['id']).then(resp => {
        this.card = resp.data
      })
    }
  }
</script>

<style scoped>

</style>

<template>
  <div>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
  import api from '../api'


  export default {
    data() {
      return {
        msg: 'waiting...'
      }
    },
    mounted: function () {
      const token = this.$route.query['token']
      if (!token) {
        this.msg = 'token not specified'
        return
      }
      api.confirm(token)
        .then(resp => {
          this.msg = `Thanks ${resp.data.name}, Email confirmed!`
        })
        .catch(_ => {
          this.msg = 'Token invalid, cannot confirm email'
        })
    }
  }
</script>

<style scoped>
  h1 {
    margin-top: 50px;
  }
</style>
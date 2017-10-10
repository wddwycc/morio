<template>
  <div>
    <el-button type="primary">主要按钮</el-button>
    <input v-model="msg">
  </div>
</template>

<script>
  export default {
    data() {
      return {
        msg: 'This is home page'
      }
    },
  }
</script>

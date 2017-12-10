<template>
  <div id="app">
    <el-menu class="menu" mode="horizontal" :default-active="$route.path" router>
      <el-menu-item index="/">Me</el-menu-item>
      <el-menu-item index="/login">Login</el-menu-item>
      <el-menu-item index="/register">Register</el-menu-item>
    </el-menu>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
    },
  }
</script>

<style>
  #app {
    max-width: 980px;
    margin: 0 auto;
  }

  .menu {
  }

  .content {
    padding: 20px;
  }
</style>


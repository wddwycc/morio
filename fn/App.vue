<template>
  <div id="app">
    <el-menu class="menu" mode="horizontal" :default-active="$route.path" router>
      <el-menu-item index="/">Me</el-menu-item>
      <el-menu-item index="/login" class="menu__login">Login</el-menu-item>
      <el-menu-item index="/register" class="menu__login">Register</el-menu-item>
    </el-menu>
    <router-view></router-view>
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
    margin-bottom: 20px;
  }
  .menu__login {
    float: right;
  }
</style>


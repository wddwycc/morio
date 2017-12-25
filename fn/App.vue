<template>
  <div id="app">
    <div class="menu">
    <ul class="menu--left" >
        <router-link to="/" tag="li" class="menu__item">Home</router-link>
    </ul>
    <ul class="menu--right">
        <router-link to="/login" tag="li" class="menu__item">Login</router-link>
        <router-link to="/register" tag="li" class="menu__item">Register</router-link>
    </ul>
    </div>
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
    display: flex;
    height: 50px;
    box-sizing: border-box;
    justify-content: space-between;
    align-items: center;
    border-bottom: solid 1px var(--color-x-light-grey);
  }

  .menu--left {
    display: flex;
    height: 100%;
    box-sizing: border-box;
    align-items: center;
  }

  .menu--right {
    display: flex;
    height: 100%;
    box-sizing: border-box;
    align-items: center;
  }

  .menu__item {
    display: inline;
    padding: 10px;
    text-align: center;
  }

  .router-link-exact-active {
    border-bottom:solid 2px var(--color-blue);
  }

  .content {
    padding: 20px;
  }
</style>


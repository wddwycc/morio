<template>
  <div id="app">
    <nav class="menu">
      <div class="menu__inner">
        <ul class="menu__left">
          <router-link to="/" tag="li" class="menu__item dim logo">Morio</router-link>
        </ul>
        <div class="menu__right" v-if="!this.$store.state.user.loading">
          <ul class="menu__login" v-if="this.$store.state.user.name">
            <router-link to="/new" tag="li" class="el-icon-plus dim menu__item"></router-link>
            <li class="menu__avatar" :style="{ backgroundImage: `url(${this.$store.state.user.avatar})`}"></li>

            <li class="menu__item">
              <el-dropdown trigger="click" @command="handleDropdown" :show-timeout="0" :hide-timeout="0">
                <span>
                  {{ this.$store.state.user.name }} <i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item command="toProfile">Your Profile</el-dropdown-item>
                  <el-dropdown-item divided command="logout">Logout</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </li>
          </ul>
          <ul class="menu__visitor" v-else>
            <router-link to="/login" tag="li" class="menu__item">Login</router-link>
            <router-link to="/register" tag="li" class="menu__item">Register</router-link>
          </ul>
        </div>
      </div>
    </nav>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import api from './api'
  import db from './store/db'

  export default {
    methods: {
      toProfile() {
        this.$router.push(`/user/${this.$store.state.user.name}`)
      },
      logout() {
        db.del('authToken')
        this.$store.commit('dropUser')
        this.$router.push('/')
      },
      handleDropdown(cmd) {
        this[cmd]()
      }
    },
    mounted: function () {
      const token = db.get('authToken')
      if (!token) {
        this.$store.commit('loadUser', null)
      }
      api.me().then(resp => {
        this.$store.commit('loadUser', resp.data)
      }, () => {
        this.$store.commit('loadUser', null)
      })
    }
  }
</script>

<style>
  #app {
  }

  .menu {
    border-bottom: solid 1px var(--color-x-light-grey);
  }

  .menu__inner {
    max-width: 980px;
    margin: 0 auto;
    display: flex;
    list-style-type: none;
    height: 50px;
    box-sizing: border-box;
    justify-content: space-between;
    align-items: center;
  }

  .menu__left {
    display: flex;
    height: 100%;
    box-sizing: border-box;
    align-items: center;
  }

  .menu__right {
    display: flex;
    list-style-type: none;
    height: 100%;
    box-sizing: border-box;
    align-items: center;
  }

  .menu__visitor {
    display: flex;
    height: 100%;
    list-style-type: none;
    align-items: center;
  }

  .menu__login {
    display: flex;
    height: 100%;
    list-style-type: none;
    align-items: center;
  }

  .menu__avatar {
    width: 20px;
    height: 20px;
    margin: 0 10px;
    background-size: cover;
  }

  .menu__item {
    height: 40px;
    line-height: 40px;
    padding: 0 10px;
    box-sizing: border-box;
    display: block;
    color: var(--color-grey);
    text-align: center;
    font-size: var(--size-small);
    cursor: pointer;
  }

  .menu__item.logo {
    font-weight: bold;
    font-size: var(--size-large);
    color: var(--color-black);
  }

  .content {
    max-width: 980px;
    margin: 0 auto;
    padding: 20px;
  }
</style>


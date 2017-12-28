<template>
  <div id="app">
    <div class="menu">
      <ul class="menu__left">
        <router-link to="/" tag="li" class="menu__item dim logo">Morio</router-link>
      </ul>
      <div class="menu__right" v-if="!this.$store.state.user.loading">
        <ul class="menu__login" v-if="this.$store.state.user.name">
          <router-link to="/new" tag="li" class="el-icon-plus dim menu__item"></router-link>
          <li class="menu__item">
            <el-dropdown @command="handleDropdown" class="menu__item">
                <span class="el-dropdown-link"> {{ this.$store.state.user.name }} <i class="el-icon-arrow-down"></i>
                </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="toSetting">Setting</el-dropdown-item>
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
      toSetting() {
        this.$router.push('/setting')
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
    max-width: 980px;
    margin: 0 auto;
  }

  .menu__item.logo {
    font-weight: bold;
    font-size: var(--size-large);
    color: var(--color-black);
  }

  .menu {
    display: flex;
    list-style-type: none;
    height: 50px;
    box-sizing: border-box;
    justify-content: space-between;
    align-items: center;
    border-bottom: solid 1px var(--color-x-light-grey);
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

  .content {
    padding: 20px;
  }
</style>


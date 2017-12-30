<template>
  <div class="user">
    <aside class="user__aside" v-if="loadingUser">
      loading...
    </aside>
    <aside class="user__aside" v-else>
      <img class="user__avatar" :src="user.avatar">
      <h1 class="user__nickname">{{ user.nickname }}</h1>
      <div class="user__name">@{{ user.name }}</div>
    </aside>


    <main class="user__main">
      <el-tabs v-model="activeTab" @tab-click="handleTabClick">
        <el-tab-pane label="Repositories" name="repos">
          <repo-cell v-for="repo in repos" :data="repo" :key="repo.id"></repo-cell>
        </el-tab-pane>
        <el-tab-pane label="Stars" name="stars">
        </el-tab-pane>
      </el-tabs>
    </main>
  </div>
</template>

<script>
  import api from '../api/index'

  export default {
    data() {
      return {
        loadingUser: true,
        user: {},
        loadingRepos: true,
        repos: [],
        // repo & fav
        activeTab: null,
        tabs: ['repos', 'stars'],
      }
    },
    computed: {
      username: function () {
        return this.$route.params['username']
      }
    },
    methods: {
      handleTabClick() {
        this.$router.push({query: {...this.$route.query, tab: this.activeTab}})
      },
      fetchRepos() {
        api.getUser(this.username).then(resp => {
          this.user = resp.data
          this.loadingUser = false
        })
        api.getRepos(this.username).then(resp => {
          this.repos = resp.data
          this.loadingRepos = false
        })
      },
      syncTab() {
        const tab = this.$route.query['tab']
        if (this.tabs.includes(tab)) {
          this.activeTab = tab
        } else {
          this.activeTab = 'repos'
        }
      }
    },
    mounted: function () {
      this.fetchRepos()
      this.syncTab()
    },
    watch: {
      '$route'() {
        this.syncTab()
      }
    }
  }
</script>

<style>
  .user {
  }

  .user__aside {
    float: left;
    margin-right: 20px;
    width: 160px;
  }

  .user__nickname {
    margin: 0;
    font-size: var(--size-extra-large);
  }

  .user__name {
    font-size: var(--size-medium);
    color: var(--color-grey);
  }

  .user__avatar {
    width: 128px;
    height: auto;
  }

  .user__main {
    overflow: hidden;
  }

</style>
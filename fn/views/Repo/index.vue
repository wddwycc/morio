<template>
  <div class="repo">
    <div v-if="!loading">
      <h1>
        <router-link :to="{name: 'User', params: { username: repo.username }}">{{ repo.username }}</router-link>
        / {{ repo.name }}
      </h1>

      <div v-if="isOwner" class="repo__top-right">
        <el-button v-if="!editing" type="primary" icon="el-icon-plus" size="mini" @click="editing = true">Card</el-button>
        <el-button v-else icon="el-icon-close" size="mini" @click="editing = false">End Edit</el-button>
        <el-button icon="el-icon-plus" size="mini" @click="newCourse()">Course</el-button>
      </div>

      <transition name="fade">
        <div class="repo-editor" v-if="editing">
          <el-row class="demo-autocomplete">
            <el-col :span="11">
              <el-input
                type="textarea"
                :rows="2"
                :placeholder="repo['side_a_name'] || 'Side A'"
                v-model="editorForm.side_a">
              </el-input>
            </el-col>
            <el-col :span="11" :offset="2">
              <el-input
                type="textarea"
                :rows="2"
                :placeholder="repo['side_b_name'] || 'Side B'"
                v-model="editorForm.side_b">
              </el-input>
            </el-col>
          </el-row>
          <el-button class="repo-editor__submit" size="mini" @click="newCard()">Add</el-button>
        </div>
      </transition>

      <el-tabs v-model="activeTab" @tab-click="handleTabClick">
        <el-tab-pane label="Cards" name="cards"></el-tab-pane>
        <el-tab-pane label="Setting" name="setting"></el-tab-pane>
      </el-tabs>

      <router-view :cards="this.cards" :repo="this.repo" :isOwner="this.isOwner"></router-view>
    </div>
  </div>
</template>

<script>
  import api from '../../api/index'
  import {Message} from 'element-ui'

  export default {
    data() {
      return {
        editing: false,
        editorForm: {
          side_a: '',
          side_b: '',
        },
        loading: true,
        // cards, setting
        activeTab: 'cards',
        repo: {},
        cards: [],
      }
    },
    computed: {
      isOwner: function () {
        return this.$store.state.user.name === this.repo.username
      },
    },
    methods: {
      newCard: function () {
        api.newCard(
          {repository_id: this.repo.id, ...this.editorForm}
        ).then(() => {
          this.editorForm.side_a = ''
          this.editorForm.side_b = ''
          Message.success('Created card')
          api.getCards(
            this.repo.username, this.repo.name
          ).then(resp => {
            this.cards = resp.data
          })
        })
      },
      handleTabClick: function () {
        if (this.activeTab === 'cards') {
          this.$router.push(`/user/${this.repo.username}/${this.repo.name}`)
        } else {
          this.$router.push(`/user/${this.repo.username}/${this.repo.name}/setting`)
        }
      },
      reloadRepo: function () {
        api.getRepo(
          this.$route.params['username'],
          this.$route.params['repo_name'],
        ).then(resp => {
          this.repo = resp.data
        })
      },
      reloadCards: function () {
        api.getCards(
          this.repo.username, this.repo.name
        ).then(resp => {
          this.cards = resp.data
          this.loading = false
        })
      },
      newCourse: function () {
        api.newCourse({repository_id: this.repo.id}).then(() => {
          Message.success('created new course')
          this.$router.push('/')
        })
      },
    },
    mounted: function () {
      if (this.$route.name === 'Repo') {
        this.activeTab = 'cards'
      } else {
        this.activeTab = 'setting'
      }
      api.getRepo(
        this.$route.params['username'],
        this.$route.params['repo_name'],
      ).then(resp => {
        this.repo = resp.data
        api.getCards(
          this.repo.username, this.repo.name
        ).then(resp => {
          this.cards = resp.data
          this.loading = false
        })
      })
    }
  }
</script>

<style>
  .repo {
    position: relative;
  }

  .repo__top-right {
    position: absolute;
    top: 8px;
    right: 0;
  }

  .repo-editor {
    margin: 20px 0;
  }

  .repo-editor__submit {
    margin-top: 10px;
  }
</style>


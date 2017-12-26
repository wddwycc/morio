<template>
  <div class="repo">
    <div v-show="!loading">
      <h1>
        <!--todo: replace with load function-->
        <router-link :to="{name: 'User', params: { username: repo.username }}">{{ repo.username }}</router-link>
        / {{ repo.name }}
      </h1>

      <div v-if="isOwner" class="repo__top-right">
        <el-button v-if="!editing" type="primary" icon="el-icon-plus" size="mini" @click="editing = true">Edit</el-button>
        <el-button v-if="editing" icon="el-icon-close" size="mini" @click="editing = false">Exit Edit</el-button>
        <!--<el-button icon="el-icon-setting" size="mini">Setting</el-button>-->
      </div>

      <transition name="fade">
        <div class="repo-editor" v-if="editing">
          <el-row class="demo-autocomplete">
            <el-col :span="11">
              <el-input
                type="textarea"
                :rows="2"
                placeholder="Side A"
                v-model="editorForm.side_a">
              </el-input>
            </el-col>
            <el-col :span="11" :offset="2">
              <el-input
                type="textarea"
                :rows="2"
                placeholder="Side B"
                v-model="editorForm.side_b">
              </el-input>
            </el-col>
          </el-row>
          <el-button class="repo-editor__submit" size="mini" @click="newCard()">Add</el-button>
        </div>
      </transition>

      <el-card v-for="card in cards" :key="card.id">
        <div slot="header">
          {{ card['side_a'] }}
        </div>
        <div>
          {{ card['side_b'] }}
        </div>
        <div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  import api from '../api'
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
        repo: {},
        cards: []
      }
    },
    computed: {
      isOwner: function () {
        // todo: replace with vuex
        return this.repo.username === 'duan'
      }
    },
    methods: {
      newCard: function () {
        api.newCard(
          {repository_id: this.repo.id, ...this.editorForm}
        ).then(() => {
          Message.success('Created card')
          api.getCards(
            this.repo.username, this.repo.name
          ).then(resp => {
            this.cards = resp.data
          })
        })
      }
    },
    mounted: function () {
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


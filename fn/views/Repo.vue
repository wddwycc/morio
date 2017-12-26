<template>
  <div class="repo">
    <div v-show="!loading">
      <h1>
        <!--todo: replace with load function-->
        <router-link :to="{name: 'User', params: { username: $route.params['username'] }}">{{ $route.params['username'] }}</router-link>
        / {{ $route.params['repo_name'] }}
      </h1>

      <div class="repo__top-right">
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
                v-model="editor.sideA">
              </el-input>
            </el-col>
            <el-col :span="11" :offset="2">
              <el-input
                type="textarea"
                :rows="2"
                placeholder="Side B"
                v-model="editor.sideB">
              </el-input>
            </el-col>
          </el-row>
          <el-button @click="editing = false">End Edit</el-button>
        </div>
      </transition>

      <el-card v-for="card in cards" :key="card.id">
        <div slot="header">
          {{ card.name }}
        </div>
        <div>
          {{ card.question }}
        </div>
        <div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  import api from '../api'

  export default {
    data() {
      return {
        editing: false,
        editor: {
          sideA: '',
          sideB: '',
        },
        form: {
          sideA: '',
          sideB: '',
        },
        loading: true,
        repo: {},
        cards: [
          {
            id: 1,
            name: '你好',
            question: 'hello',
          },
          {
            id: 2,
            name: '再见',
            question: 'bye',
          }
        ]
      }
    },
    computed: {},
    methods: {
      getRepo: function () {
        api.getRepo(this.$route.params['username'],
          this.$route.params['repo_name']).then(resp => {
          this.repo = resp.data
          this.loading = false
        })
      },
      newCard: function () {
        api.newCard($route.params['repo_name'])
      }
    },
    mounted: function () {
      this.getRepo()
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

</style>


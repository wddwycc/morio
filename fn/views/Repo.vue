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
        <div class="repo-editor" v-show="editing">
          <el-row class="demo-autocomplete">
            <el-input
              v-for="i in ['a', 'b', 'c', 'd', 'e', 'f'].slice(0, repo.sides)"
              :key="i"
              type="textarea"
              class="editor__entity"
              :rows="2"
              :placeholder="repo[`side_${i}_name`] || `Side ${i.toUpperCase()}`"
              v-model="editorForm[`side_${i}`]">
            </el-input>
          </el-row>
          <el-button class="repo-editor__submit" size="mini" @click="newCard()">Add</el-button>
        </div>
      </transition>

      <el-tabs v-model="activeTab">
        <el-tab-pane label="Cards" name="cards">
          <div v-if="cards.length > 0">
            <el-card v-for="card in cards" :key="card.id" class="card">
              <div v-for="i in ['a', 'b', 'c', 'd', 'e', 'f'].slice(0, repo.sides)">
                <p class="card__key">{{ repo[`side_${i}_name`] || `Side ${i.toUpperCase()}` }}:</p>
                <p class="card__value">{{ card[`side_${i}`] }}</p>
              </div>
              <el-button v-if="isOwner" class="card__del" icon="el-icon-delete" size="mini" type="text" @click="delCard(card.id)"></el-button>
            </el-card>

            <el-pagination
              class="pagination"
              layout="prev, pager, next"
              :total=this.total :page-size="limit" :current-page="currentPage"
              @current-change="onPageChange">
            </el-pagination>
          </div>
          <empty text="No card" v-else></empty>
        </el-tab-pane>
        <el-tab-pane v-if="isOwner" label="Setting" name="setting">
          <el-form ref="settingForm" :model="settingForm" label-width="80px" label-position="right" class="register">
            <el-form-item label="Private">
              <el-switch v-model="settingForm.private"></el-switch>
            </el-form-item>
            <el-form-item label="Description" prop="desc">
              <el-input type="textarea" v-model="settingForm.desc"></el-input>
            </el-form-item>

            <el-form-item label="Sides">
              <el-input-number v-model="settingForm.sides" controls-position="right" :min="2" :max="6"></el-input-number>
            </el-form-item>

            <el-form-item label="Side A" prop="side_a_name">
              <el-input v-model="settingForm.side_a_name"></el-input>
            </el-form-item>
            <el-form-item label="Side B" prop="side_b_name">
              <el-input v-model="settingForm.side_b_name"></el-input>
            </el-form-item>
            <el-form-item v-if="settingForm.sides >= 3" label="Side C" prop="side_c_name">
              <el-input v-model="settingForm.side_c_name"></el-input>
            </el-form-item>
            <el-form-item v-if="settingForm.sides >= 4" label="Side D" prop="side_d_name">
              <el-input v-model="settingForm.side_d_name"></el-input>
            </el-form-item>
            <el-form-item v-if="settingForm.sides >= 5" label="Side E" prop="side_e_name">
              <el-input v-model="settingForm.side_e_name"></el-input>
            </el-form-item>
            <el-form-item v-if="settingForm.sides >= 6" label="Side F" prop="side_f_name">
              <el-input v-model="settingForm.side_f_name"></el-input>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="onSubmitSetting()">Save</el-button>
            </el-form-item>
          </el-form>

        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import api from '../api/index'
  import {Message} from 'element-ui'

  export default {
    data() {
      return {
        editing: false,
        editorForm: {
          side_a: '',
          side_b: '',
          side_c: '',
          side_d: '',
          side_e: '',
          side_f: '',
        },
        settingForm: {
          desc: '',
          private: false,
          sides: 2,
          side_a_name: null,
          side_b_name: null,
          side_c_name: null,
          side_d_name: null,
          side_e_name: null,
          side_f_name: null,
        },
        loading: true,
        activeTab: 'cards',
        repo: {},
        cards: [],
        limit: 30,
        currentPage: 1,
        total: 0,
      }
    },
    computed: {
      isOwner: function () {
        return this.$store.state.user.name === this.repo.username
      },
      offset: function () {
        return this.limit * (this.currentPage - 1)
      },
    },
    methods: {
      newCard: function () {
        api.newCard(
          {repository_id: this.repo.id, ...this.editorForm}
        ).then(() => {
          for (let i of ['a', 'b', 'c', 'd', 'e', 'f']) {
            this.editorForm[`side_${i}`] = ''
          }
          Message.success('Created card')
          this.reloadCards()
        })
      },
      delCard(id) {
        api.delCard(id).then(() => {
          Message.success('Deleted')
          this.reloadCards()
        })
      },
      reloadCards: function () {
        api.getCards(
          this.repo.username, this.repo.name,
          {limit: this.limit, offset: this.offset}
        ).then(resp => {
          this.total = resp.data.total
          this.cards = resp.data.data
          this.loading = false
        })
      },
      onPageChange: function (target) {
        api.getCards(
          this.repo.username, this.repo.name,
          {limit: this.limit, offset: (target - 1) * this.limit}
        ).then(resp => {
          this.total = resp.data.total
          this.cards = resp.data.data
          this.currentPage = target
        })
      },
      newCourse: function () {
        api.newCourse({repository_id: this.repo.id}).then(() => {
          Message.success('created new course')
          this.$router.push('/')
        })
      },
      onSubmitSetting: function () {
        api.updateRepo(this.repo.id, this.settingForm).then(resp => {
          Message.success('Updated')
          this.repo = resp.data
        })
      },
    },
    beforeRouteEnter: function (to, from, next) {
      api.getRepo(
        to.params['username'],
        to.params['repo_name'],
      ).then(resp => {
        next(vm => {
          vm['repo'] = resp.data
          vm['settingForm'] = Vue.util.extend({}, resp.data)
          vm.reloadCards()
        })
      })
    },
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

  .card {
    margin-bottom: 10px;
    position: relative;
  }

  .card__key {
    color: var(--color-light-grey);
  }

  .card__value {
    margin: 10px 0;
    word-wrap: break-word;
    color: var(--color-black);
  }

  .card__del {
    position: absolute;
    top: 16px;
    right: 16px;
  }

  .editor__entity {
    margin-bottom: 10px;
  }

  .pagination {
    margin: 0 auto;
  }

</style>

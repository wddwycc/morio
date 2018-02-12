<template>
  <div v-if="repo">
    <h1>New course for
      <router-link :to="{ name: 'Repo', params: { username: repo.username, repo_name: repo.name }}" tag="a">
        {{ repo.username }}/{{ repo.name }}
      </router-link>
    </h1>

    <el-form ref="form" :model="form" label-width="80px" label-position="top">
      <el-form-item label="Name" required>
        <el-input v-model="form.name"></el-input>
      </el-form-item>

      <el-form-item label="Max Daily new cards" required>
        <el-input-number v-model="form.daily_new" controls-position="right" :min="1" :max="1000"></el-input-number>
      </el-form-item>

      <el-form-item label="Max Daily review cards" required>
        <el-input-number v-model="form.daily_review" controls-position="right" :min="1" :max="1000"></el-input-number>
      </el-form-item>

      <el-form-item label="Q&A Sides" required>
        <el-transfer v-model="rightSides" :data="allSides" :titles="['Question Side', 'Answer Side']"></el-transfer>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit()">Create</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import api from '../api'
  import {Message} from 'element-ui'

  export default {
    data() {
      return {
        repo: null,
        form: {
          name: null,
          daily_new: 30,
          daily_review: 180,
        },
        rightSides: ['b'],
      }
    },
    computed: {
      allSides: function () {
        let repo = this.repo
        if (!repo) {
          return []
        }
        return ['a', 'b', 'c', 'd', 'e', 'f']
          .slice(0, repo.sides)
          .map(i => {
            return {
              key: i,
              label: repo[`side_${i}_name`] || `${i.toUpperCase()} Side`,
            }
          })
      },
    },
    methods: {
      onSubmit: function () {
        let all_sides = this.allSides.map(v => v.key)
        let q_sides = all_sides
          .concat(this.rightSides)
          .filter(v => !all_sides.includes(v) || !this.rightSides.includes(v))
          .join(',')
        let a_sides = this.rightSides.join(',')
        api.newCourse({repository_id: this.repo.id, q_sides, a_sides, ...this.form})
          .then(resp => {
            Message.success('created new course')
            this.$router.push(`/course/${resp.data.id}`)
          })
      }
    },
    beforeRouteEnter: function (to, from, next) {
      let repoId = to.query['repoId']
      if (!repoId) {
        return next('/')
      }
      api.getRepoById(repoId)
        .then(resp => {
          next(vm => {
            vm['repo'] = resp.data
          })
        })
        .catch(_ => {
          return next('/')
        })
    },
  }
</script>

<style scoped>

</style>
<template>
  <el-form ref="form" :rules="rules" :model="form" label-width="80px" label-position="right" class="register" @keyup.enter.native="onSubmit()">
    <el-form-item label="Private">
      <el-switch v-model="form.private"></el-switch>
    </el-form-item>
    <el-form-item label="Description" prop="desc">
      <el-input type="textarea" v-model="form.desc"></el-input>
    </el-form-item>

    <el-form-item label="Side A" prop="side_a_name">
      <el-input v-model="form.side_a_name"></el-input>
    </el-form-item>
    <el-form-item label="Side B" prop="side_b_name">
      <el-input v-model="form.side_b_name"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit()">Save</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import {Message} from 'element-ui'
  import Vue from 'vue'
  import api from '../../api'

  export default {
    props: ['repo'],
    data() {
      return {
        form: Vue.util.extend({}, this.repo),
        rules: {},
      }
    },
    methods: {
      onSubmit: function () {
        api.updateRepo(this.repo.username, this.repo.name, this.form).then(() => {
          Message.success('Updated')
          this.$parent.reloadRepo()
        })
      }
    }
  }
</script>

<style scoped>

</style>

<template>
  <div>
    <h1>Login</h1>
    <el-form ref="form" :rules="rules" :model="form" label-width="80px" label-position="right" class="form">
      <el-form-item label="User" prop="user" required>
        <el-input v-model="form.user"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password" required>
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">Login</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import {Message} from 'element-ui'
  import api from '../api'

  export default {
    data() {
      return {
        form: {
          user: '',
          password: '',
        },
        rules: {},
      }
    },
    methods: {
      onSubmit() {
        this.$refs['form'].validate((valid) => {
          if (!valid) {
            return
          }
          api.login(this.form).then(resp => {
            Message.success(`Welcome back, ${resp.data.name}`)
            this.$store.commit('loadUser', resp.data)
            this.$router.push('/')
          })
        })
      },
    },
  }
</script>

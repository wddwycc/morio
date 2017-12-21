<template>
  <div>
    <el-form ref="form" :rules="rules" :model="form" label-width="100px" label-position="right" class="register">
      <el-form-item label="Email" prop="email" required>
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="Username" prop="name" required>
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Nickname" prop="nickname" required>
        <el-input v-model="form.nickname"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password" required>
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item label="Confirm" prop="passwordConfirmed" required>
        <el-input type="password" v-model="form.passwordConfirmed"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">Register</el-button>
        <el-button @click="onReset()">Reset</el-button>
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
          email: '',
          name: '',
          nickname: '',
          password: '',
          passwordConfirmed: '',
        },
        rules: {
          name: [],
        }
      }
    },
    methods: {
      onSubmit() {
        this.$refs['form'].validate((valid) => {
          if (!valid) {
            return
          }
          api.register(this.form).then(() => {
            Message.success('Register success')
            this.$router.push('/')
          })
        })
      },
      onReset() {
        this.$refs['form'].resetFields()
      }
    }
  }
</script>

<style>
  .register {
    max-width: 460px;
  }
</style>

<template>
  <div>
    <h1>New Repository</h1>

    <el-form ref="form" :rules="rules" :model="form" label-width="80px" label-position="right" class="register">
      <el-form-item label="Name" prop="name" required>
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Description" prop="desc">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item label="Private" required>
        <el-switch v-model="form.private"></el-switch>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">Create</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import api from '../api'

  export default {
    data() {
      return {
        form: {
          name: '',
          desc: '',
          private: '',
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
          api.newRepo(this.form).then(resp => {
            this.$router.push('/')
          })
        })
      },
    },
  }
</script>

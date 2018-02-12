<template>
  <div>
    <h1>New Repository</h1>

    <el-form ref="form" :rules="rules" :model="form" label-width="80px" label-position="right" class="form">
      <el-form-item label="Name" prop="name" required>
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Description" prop="desc">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item label="Private" required>
        <el-switch v-model="form.private"></el-switch>
      </el-form-item>

      <el-form-item label="Sides" required>
        <el-input-number v-model="form.sides" controls-position="right" :min="2" :max="6"></el-input-number>
      </el-form-item>

      <el-form-item v-for="i in ['a', 'b', 'c', 'd', 'e', 'f'].slice(0, form.sides)" :key="i" :label="`Side ${i.toUpperCase()}`" :prop="`side_${i}_name`">
        <el-input v-model="form[`side_${i}_name`]"></el-input>
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
          sides: 2,
          private: false,
          side_a_name: null,
          side_b_name: null,
          side_c_name: null,
          side_d_name: null,
          side_e_name: null,
          side_f_name: null,
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
            this.$router.push(`/user/${resp.data.username}/${resp.data.name}`)
          })
        })
      },
    },
  }
</script>

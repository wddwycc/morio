<template>
  <div>
    <div v-if="!loading && courses.length === 0 && repos.length === 0">
      This is landing page
      <!--  todo: landing page -->
    </div>
    <div v-else>
      <div v-if="courses.length > 0">
        <h2>Courses</h2>
        <el-card class="course-cell" v-for="course in courses" :key="course.id">
          <div>Learn {{ course['repository']['username'] }}/{{ course['repository']['name'] }}</div>
          <el-button class="course-cell__del" icon="el-icon-delete" size="mini" type="text" @click="delCourse(course.id)"></el-button>
        </el-card>
      </div>
      <div v-if="repos.length > 0">
        <h2>Repositories</h2>
        <repo-cell v-for="repo in repos" :data="repo" :key="repo.id"></repo-cell>
      </div>
    </div>


    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>Please confirm your request</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible = false">Yes</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import api from '../api'
  import db from '../store/db'

  export default {
    data() {
      return {
        loadingCourses: true,
        courses: [],
        loadingRepos: true,
        repos: [],
        dialogVisible: false,
      }
    },
    computed: {
      loading: function () {
        return this.loadingCourses || this.loadingRepos
      }
    },
    methods: {
      fetchRepos() {
        api.myRepos().then(resp => {
          this.repos = resp.data
          this.loadingRepos = false
        })
      },
      fetchCourses() {
        api.myCourses().then(resp => {
          this.courses = resp.data
          this.loadingCourses = false
        })
      },
      delCourse(id) {
        this.$confirm('Are you sure to delete course')
          .then(() => {
            api.delCourse(id).then(() => {
              this.fetchCourses()
            })
          })
          .catch(_ => {})
      }
    },
    mounted: function () {
      const token = db.get('authToken')
      if (!token) {
        this.loadingCourses = false
        this.loadingRepos = false
        return
      }
      this.fetchRepos()
      this.fetchCourses()
    }
  }
</script>

<style>
  .course-cell {
    margin-bottom: 10px;
    position: relative;
  }

  .course-cell__del {
    position: absolute;
    top: 16px;
    right: 16px;
  }
</style>

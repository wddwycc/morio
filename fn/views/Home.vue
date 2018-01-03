<template>
  <div>
    <div v-if="!loading && courses.length === 0 && repos.length === 0">
      <div class="lp__top">
        <div class="lp__logo"></div>
        <div>
          <h1 class="lp__title">Morio</h1>
          <h2 class="lp__subtitle">Web service for memory</h2>
          <p>Memorizing norms and concepts is usually necessary when entering a new area.</p>
          <p>If inefficient, it would be painful and do harm to one's passion.</p>
          <p>Morio borns to bridge the gap.</p>
        </div>
      </div>
      <ul class="lp__features">
        <li class="lp__feature">
          <div class="lp__icon" :style="{backgroundImage : `url(${require('../assets/sprout.png')})` }"></div>
          <div>
            <h2 class="lp__feature-name">Free</h2>
            <p>Customize contents and corresponding ways you want to memorize</p>
          </div>
        </li>
        <li class="lp__feature">
          <div class="lp__icon" :style="{backgroundImage : `url(${require('../assets/flask.png')})` }"></div>
          <div>
            <h2 class="lp__feature-name">Efficiency</h2>
            <p>Memorize everything through proper methodology like forgetting curve</p>
          </div>
        </li>
        <li class="lp__feature">
          <div class="lp__icon" :style="{backgroundImage : `url(${require('../assets/globe.png')})` }"></div>
          <div>
            <h2 class="lp__feature-name">Community</h2>
            <p>Share your knowledge base and search your interested repository here</p>
          </div>
        </li>
      </ul>
    </div>
    <div v-else>
      <div v-if="courses.length > 0">
        <h2>Courses</h2>
        <el-card class="course-cell" v-for="course in courses" :key="course.id">
          <router-link :to="{name: 'Course', params: { id: course.id }}">
            <el-button type="text">Learn {{ course['repository']['username'] }}/{{ course['repository']['name'] }}</el-button>
          </router-link>
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
          .catch(_ => {
          })
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
  .lp__top {
    max-width: 880px;
    margin: 100px auto 100px;
    display: flex;
    justify-content: center;
  }

  .lp__logo {
    width: 200px;
    height: 200px;
    margin-right: 20px;
    background: url('../assets/logo_512.png') no-repeat;
    background-size: contain;
  }

  .lp__title {
    font-size: 2.4em;
    padding: 0;
    margin-bottom: 0;
  }

  .lp__subtitle {
    margin-top: 0;
  }

  .lp__top p {
    margin: 4px 0;
    font-size: 1em;
    font-weight: 300;
    color: var(--color-grey);
  }

  .course-cell {
    margin-bottom: 10px;
    position: relative;
  }

  .course-cell__del {
    position: absolute;
    top: 16px;
    right: 16px;
  }

  .lp__features {
    display: flex;
    justify-content: space-around;
    list-style: none;
  }

  .lp__feature {
    width: 240px;
    margin: 0 20px 20px;
  }

  .lp__feature p {
    text-align: center;
    font-weight: 300;
    color: var(--color-grey);
  }

  .lp__feature-name {
    text-align: center;
  }

  .lp__icon {
    width: 64px;
    height: 64px;
    margin: 0 auto;
    background-size: contain;
    background-repeat: no-repeat;
  }

  .course-cell .el-button {
    padding: 0;
    font-size: var(--size-small);
  }

  @media screen and (max-width: 600px) {
    .lp__top {
      margin: 0 0 30px;
      flex-direction: column;
    }

    .lp__title {
      margin-top: 20px;
      font-size: 1.5em;
    }

    .lp__features {
      flex-direction: column;
    }

    .lp__feature {
      margin-left: 0;
      margin-right: 0;
      margin-bottom: 30px;
      width: auto;
      display: flex;
    }

    .lp__feature p, .lp__feature-name {
      text-align: left;
    }

    .lp__icon {
      margin: 20px 20px 0 0;
    }
  }
</style>

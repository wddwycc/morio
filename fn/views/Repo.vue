<template>
  <div class="repo">
    <h1>
      <router-link :to="{name: 'User', params: { username: $route.params['username'] }}">{{ $route.params['username'] }}</router-link> / {{ $route.params['repo_name'] }}
    </h1>

    <div class="repo__top-right">
      <el-button type="primary" icon="el-icon-plus" size="mini" @click="editing = !editing">
        Add
      </el-button>
      <!--<el-button icon="el-icon-setting" size="mini">Setting</el-button>-->
    </div>

    <div class="repo-editor" v-if="editing">
      <!-- todo: editor implementation -->
      this is a editor
    </div>

    <el-card v-for="card in repo" :key="card.id">
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
</template>

<script>
  export default {
    data() {
      return {
        editing: false,
        repo: [
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
    computed: {
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


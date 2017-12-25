<template>
  <div>
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
  }
</script>
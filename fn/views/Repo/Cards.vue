<template>
  <div>
    <el-card v-for="card in cards" :key="card.id" class="card">
      <div>
        Side A: {{ card['side_a'] }}
      </div>
      <div>
        Side B: {{ card['side_b'] }}
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    props: ['cards'],
  }
</script>

<style scoped>
  .card {
    margin-bottom: 10px;
  }
</style>

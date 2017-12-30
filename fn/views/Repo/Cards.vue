<template>
  <div>
    <el-card v-for="card in cards" :key="card.id" class="card">
      <div>
        <span class="card__key">{{ repo['side_a_name'] || 'Side A' }}:</span> <span class="card__value">{{ card['side_a'] }}</span>
      </div>
      <div>
        <span class="card__key">{{ repo['side_b_name'] || 'Side B' }}:</span> <span class="card__value">{{ card['side_b'] }}</span>
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    props: ['repo', 'cards'],
  }
</script>

<style scoped>
  .card {
    margin-bottom: 10px;
  }

  .card__key {
    color: var(--color-light-grey);
  }

  .card__value {
    color: var(--color-black);
  }
</style>

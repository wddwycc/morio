<template>
  <div>
    <div v-if="cards.length > 0">
      <el-card v-for="card in cards" :key="card.id" class="card">
        <div>
          <span class="card__key">{{ repo['side_a_name'] || 'Side A' }}:</span>
          <span class="card__value">{{ card['side_a'] }}</span>
        </div>
        <div>
          <span class="card__key">{{ repo['side_b_name'] || 'Side B' }}:</span>
          <span class="card__value">{{ card['side_b'] }}</span>
        </div>
        <el-button v-if="isOwner" class="card__del" icon="el-icon-delete" size="mini" type="text" @click="delCard(card.id)"></el-button>
      </el-card>
    </div>
    <empty text="No card" v-else></empty>
  </div>
</template>

<script>
  import api from '../../api'
  import {Message} from 'element-ui'

  export default {
    props: ['repo', 'cards', 'isOwner'],
    methods: {
      delCard(id) {
        api.delCard(id).then(() => {
          Message.success('Deleted')
          this.$parent.reloadCards()
        })
      }
    }
  }
</script>

<style scoped>
  .card {
    margin-bottom: 10px;
    position: relative;
  }

  .card__key {
    color: var(--color-light-grey);
  }

  .card__value {
    color: var(--color-black);
  }

  .card__del {
    position: absolute;
    top: 16px;
    right: 16px;
  }
</style>

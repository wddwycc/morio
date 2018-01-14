<template>
  <div>
    <div v-if="loading">
      <p>loading...</p>
    </div>
    <div v-else>
      <div v-if="card && card.repo">
        <el-card class="box-card">
          <div>
            <p class="card__key">{{ card.repo['side_a_name'] || 'Side A' }}:</p>
            <p class="card__value">{{ card['side_a'] }}</p>
          </div>
          <div v-if="showAnswer">
            <p class="card__key">{{ card.repo['side_b_name'] || 'Side B' }}:</p>
            <p class="card__value">{{ card['side_b'] }}</p>
          </div>
        </el-card>

        <el-button class="course__show-answer" @click="showAnswer = !showAnswer">
          <template v-if="showAnswer">Hide Answer</template>
          <template v-else>Show Answer</template>
        </el-button>

        <div v-if="showAnswer">
          <p class="course__prompt">How you feel?</p>
          <el-button type="primary" @click="next(0)">Easy</el-button>
          <el-button type="primary" @click="next(1)">Medium</el-button>
          <el-button type="primary" @click="next(2)">Hard</el-button>
        </div>
      </div>
      <div v-else>
        <h1>You have completed this course!</h1>
      </div>
    </div>
  </div>
</template>

<script>
  import api from '../api'

  export default {
    data() {
      return {
        card: null,
        showAnswer: false,
        loading: true,
      }
    },
    computed: {
      id: function () {
        return this.$route.params['id']
      }
    },
    methods: {
      next: function (last_choice) {
        this.loading = true
        let payload = {}
        if ((last_choice || last_choice === 0) && this.card) {
          payload = {card_id: this.card.id, type: last_choice}
        }
        api.courseNextCard(this.id, payload).then(resp => {
          this.showAnswer = false
          this.card = resp.data
          this.loading = false
        })
      },
    },
    mounted() {
      this.next()
    }
  }
</script>

<style scoped>
  .course__show-answer {
    margin: 20px 0;
  }

  .course__prompt {
    margin: 10px 0;
  }

</style>

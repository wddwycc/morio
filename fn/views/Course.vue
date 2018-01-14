<template>
  <div>
    <div v-if="loading">
      <p>loading...</p>
    </div>
    <div v-else>
      <div v-if="card && repo">
        <h1>{{ summary }}</h1>
        <el-card class="box-card">
          <div>
            <p class="card__key">{{ repo['side_a_name'] || 'Side A' }}:</p>
            <p class="card__value">{{ card['side_a'] }}</p>
          </div>
          <div v-if="showAnswer">
            <p class="card__key">{{ repo['side_b_name'] || 'Side B' }}:</p>
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
        <h1>🎉 You have no card to learn today</h1>
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
        repo: null,
        showAnswer: false,
        loading: true,
        summary: '',
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
          payload = {card_id: this.card.id, feel: last_choice}
        }
        api.courseNextCard(this.id, payload).then(resp => {
          this.showAnswer = false
          if (resp.data.data) {
            this.card = resp.data.data.card
            this.repo = resp.data.data.repo
            this.summary = `Today: ${resp.data.summary.to_learn} cards to learn, ${resp.data.summary.to_review} cards to review`
          } else {
            this.card = null
            this.repo = null
            this.summary = ''
          }
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

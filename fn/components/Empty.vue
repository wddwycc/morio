<template>
  <div class="empty">
    <div class="empty__logo"></div>
    <div class="empty__text">{{ text }}</div>
  </div>
</template>

<script>
  export default {
    name: "empty",
    props: ['text']
  }
</script>

<style scoped>
  .empty {
    margin: 0 auto;
    text-align: center;
  }

  .empty__logo {
    width: 64px;
    height: 64px;
    margin: 20px auto;
    background-image: url('../assets/empty.png');
    background-size: contain;
    opacity: .3;
  }

  .empty__text {
    color: var(--color-grey);
    font-size: var(--size-large);
  }
</style>
<template>
  <div v-if="oa && observers.length > 0">
    <span>OBSERVERS: </span>
    <span v-for="i in observers" :key="i">
      <span v-if="i === gamernick">
        YOU
      </span>
      <span v-else>
        {{i}}
      </span>
      </span>
  </div>
</template>

<script>
import store from '../store/index'
export default {
  name: 'observers',
  computed: {
    observers () {
      return store.getters.getobserve
    }
  },
  data () {
    return {
      oa: store.state.oa,
      gamernick: store.state.gamernick
    }
  }
}
</script>

<style scoped>
div{
  margin: auto;
  padding: 10px;
  border: 20px;
  background-color: aquamarine;
}
</style>

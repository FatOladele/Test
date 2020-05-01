<template>
  <div :id = 'bid' draggable="false" class= "rack" @dragover.prevent @drop.prevent = "drop">
    <slot/>
  </div>
</template>

<script>
import store from '../store'
export default {
  props: ['bid'],
  data () {
    return {
    }
  },
  methods: {
    drop: e => {
      const letterId = e.dataTransfer.getData('letterID')
      const letter = document.getElementById(letterId)
      letter.style.display = 'inline-block'
      e.target.appendChild(letter)
      const pid = e.target.id
      const position = pid.toString().substring(1)
      const letterClass = letter.classList
      var lclass = letterClass.toString().substring(1)
      lclass = parseInt(lclass)
      const lobject = [position, lclass]
      store.dispatch('addtonboardaction', lobject)
    }
  }
}
</script>

<style scoped>
  .rack{
    width : 32px;
    height: 32px;
    padding: 0;
    border : 0;
    display : inline-block
  }
</style>

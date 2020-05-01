<template>
  <div :id = 'sid' draggable="false" class= "rack" @dragover.prevent @drop.prevent = "drop">
    <slot/>
  </div>
</template>

<script>
import store from '../store'
export default {
  name: 'sslot',
  props: ['sid'],
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
      const letterClass = letter.classList
      var lclass = letterClass.toString().substring(1)
      lclass = parseInt(lclass)
      store.dispatch('addswaptile', lclass)
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
    display: inline-block;
    margin: auto
  }
</style>

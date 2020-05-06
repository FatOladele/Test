<template>
  <div :id = 'bid' draggable="false" class= "rack" @dragover.prevent @drop.prevent = "drop" @click.stop @click.prevent = "dselected">
    <slot/>
  </div>
</template>

<script>
import store from '../store'
export default {
  props: ['bid'],
  components: {
  },
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
      if (lclass < 199) {
        const lobject = [position, lclass]
        store.dispatch('addtonboardaction', lobject)
      } else {
        const lobject = [position, letterId]
        store.dispatch('addblank', lobject)
      }
    },
    dselected: e => {
      const letterId = store.state.selected.cid
      var slotid = store.state.selected.pid
      if (e.target.id !== slotid) {
        if (Object.keys(store.state.selected).length > 1) {
          const letter = document.getElementById(letterId)
          var slot = document.getElementById(slotid)
          slot.removeChild(letter)
          letter.style.display = 'inline-block'
          e.target.appendChild(letter)
          const pid = e.target.id
          const position = pid.toString().substring(1)
          const letterClass = letter.classList
          console.log(letterClass)
          var lclass = letterClass.toString().substring(1)
          console.log(lclass)
          lclass = parseInt(lclass)
          slotid = slotid.toString()
          store.dispatch('selectedtile', {})
          if (slotid[0] === 'B') {
            slotid = slotid.substring(1)
            store.dispatch('removetilea', slotid)
          } else if (slotid[1] === 's') {
            store.dispatch('removeswaptile', lclass)
          }
          if (lclass < 199) {
            const lobject = [position, lclass]
            store.dispatch('addtonboardaction', lobject)
          } else {
            const lobject = [position, letterId]
            store.dispatch('addblank', lobject)
          }
        }
      }
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

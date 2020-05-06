<template>
  <div :id = id draggable="false" class= "rack" @dragover.prevent @drop.prevent = "drop" @click.stop @click.prevent = "dselected">
    <slot/>
  </div>
</template>

<script>
import store from '../store'
export default {
  props: ['id'],
  methods: {
    drop: e => {
      const letterId = e.dataTransfer.getData('letterID')
      const letter = document.getElementById(letterId)
      letter.style.display = 'inline-block'
      e.target.appendChild(letter)
    },
    dselected: e => {
      const letterId = store.state.selected.cid
      var slotid = store.state.selected.pid
      if (e.target.id !== slotid) {
        if (Object.keys(store.state.selected).length > 1) {
          const letter = document.getElementById(letterId)
          const slot = document.getElementById(slotid)
          const letterClass = letter.classList
          var lclass = letterClass.toString().substring(1)
          lclass = parseInt(lclass)
          slot.removeChild(letter)
          letter.style.display = 'inline-block'
          e.target.appendChild(letter)
          store.dispatch('selectedtile', {})
          slotid = slotid.toString()
          if (slotid[0] === 'B') {
            slotid = slotid.substring(1)
            store.dispatch('removetilea', slotid)
          } else if (slotid[1] === 's') {
            store.dispatch('removeswaptile', lclass)
          }
          if (lclass > 199) {
            letter.classList = 'L200 letter'
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
    border : 0;
    margin: auto;
    display : inline-block
  }
</style>

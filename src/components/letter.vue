<template>
  <div :id= id :class="[letcode, 'letter']" :draggable="draggable" @dragstart="dragStart" @mousedown="aboutdrag" @dragover.stop @dragend.prevent="check">
  <slot/>
  </div>
</template>

<script>
import store from '../store'
export default {
  props: ['id', 'draggable', 'letcode'],
  data () {
    return {
      initialpos: 'a'
    }
  },
  methods: {
    dragStart: e => {
      const target = e.target
      e.dataTransfer.setData('letterID', target.id)
      setTimeout(() => {
        target.style.display = 'none'
      }, 0)
    },
    aboutdrag: e => {
      let parent = e.target.parentElement.id
      if (self.initialpos !== '') {
        if (parent[0] === 'l') {
          parent = e.target.parentElement.parentElement.id
          self.initialpos = parent
        } else {
          self.initialpos = parent
        }
      }
    },
    check: e => {
      const parent = e.target.parentElement.id
      if (parent === self.initialpos) {
        // const slot = document.getElementById(self.initialpos)
        // slot.appendChild(e.target)
        e.target.style.display = 'inline-block'
      } else {
        const slotId = self.initialpos
        var slot = slotId.toString()
        if (slot[0] === 'B') {
          slot = slot.substring(1)
          store.dispatch('removetilea', slot)
        } else if (slot[0] === 's') {
          const letter = e.target.classList
          var lclass = letter.toString().substring(1)
          store.dispatch('removeswaptile', lclass)
        }
      }
    }
  }
}
</script>

<style scoped>
  .letter{
    width: 32px;
    height: 32px;
    padding: 0;
    margin: auto;
    border: 3px;
    /* background-color: green; */
    cursor: pointer;
    display : inline-block;
    z-index: 9;
  }
  .L111{
    background-image: url("../assets/Alphabet/111.jpg");
    background-repeat: no-repeat;
  }
  .L112{
    background-image: url("../assets/Alphabet/112.jpg");
    background-repeat: no-repeat;
  }
  .L113{
    background-image: url("../assets/Alphabet/113.jpg");
    background-repeat: no-repeat;
  }
  .L114{
    background-image: url("../assets/Alphabet/114.jpg");
    background-repeat: no-repeat;
  }
  .L115{
    background-image: url("../assets/Alphabet/115.jpg");
    background-repeat: no-repeat;
  }
  .L116{
    background-image: url("../assets/Alphabet/116.jpg");
    background-repeat: no-repeat;
  }
  .L117{
    background-image: url("../assets/Alphabet/117.jpg");
    background-repeat: no-repeat;
  }
</style>

<template>
  <div :id = id draggable="false" class= "rack" @dragover.prevent @drop.prevent = "drop">
    <slot/>
  </div>
</template>

<script>
export default {
  props: ['id'],
  methods: {
    drop: e => {
      const letterId = e.dataTransfer.getData('letterID')
      const letter = document.getElementById(letterId)
      letter.style.display = 'inline-block'
      e.target.appendChild(letter)
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

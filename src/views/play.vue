<template>
  <div class = "maingame">
    <div class = "room">
      <room/>
    </div>
    <div class = 'info'>
      <info/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import room from '@/components/playroom.vue'
import info from '@/components/Info.vue'
export default {
  name: 'game',
  components: {
    room,
    info
  }
}
</script>

<style scoped>
  .game td{
    height: 5rem;
    width: 5rem;
    border: 2px solid white;
    text-align: center;
    font-size: 2rem;
    /*padding: 2px;*/
  }
  .game{
    height: 1000px;
    width: 1000px;
    border: 2px solid black;
  }
  .maingame{
    display: inline-flex;
    justify-items: auto;
    width: 100%;
  }
  .room{
    margin: 10px;
  }
  .info{
    vertical-align: center;
    margin: 10px;
    align-items: center;
    border: 2px solid black;
    background-color: aquamarine;
    padding: 5px
  }
</style>

<template>
  <div >
    <table class="table">
      <tr>
        <td colspan="3" class = "hrack">
          <hrack v-if = 'onick.length > 1' :col = 'colourcode[opponent[onick[1]]["id"]]'></hrack>
        </td>
      </tr>
      <tr>
        <td class = "vrack">
          <vrack v-if = 'onick.length > 0' :col = 'colourcode[opponent[onick[0]]["id"]]'></vrack>
        </td>
        <td class = "board">
          <board/>
        </td>
        <td class ="vrack">
          <vrack v-if = 'onick.length > 2' :col = 'colourcode[opponent[onick[2]]["id"]]'></vrack>
        </td>
      </tr>
      <tr>
        <td colspan="3" class = "hrack">
          <prack :col = 'colourcode[player["id"]]'></prack>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import Board from './Board.vue'
import hrack from './hrack.vue'
import vrack from './vrack.vue'
import prack from './prack.vue'
import store from '../store/index'
export default {
  name: 'Table',
  components: {
    Board,
    hrack,
    vrack,
    prack
  },
  data () {
    return {
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      },
      onick: Object.keys(store.state.opponent),
      opponent: store.state.opponent,
      player: store.state.player
    }
  }
}
</script>

<style scoped>
  table {
    border-collapse: collapse ;
    border: 3px rgb(78, 33, 33) solid ;
    border-collapse: collapse ;
    background: rgb(78, 33, 33);
  }
  .table{
    height: 710px;
    width: 710px;
  }
  .board{
    height: 600px;
    width: 600px;
    align-items: center;
  }
  .vrack{
    width: 50px;
    height: 600px;
  }
  .hrack{
    height: 50px;
    width: 700px;
  }
  .table td {
    border: 1px solid rgb(78, 33, 33);
    text-align: center;
    font-size: 1rem;
    margin: auto;
    /*padding: 2px;*/
  }
</style>

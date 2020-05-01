<template >
  <div class="main">
    <div class="game">
      <table>
        <tr>
          <td colspan="3">
            <vpinfo v-if = 'onick.length > 1' :id= 'opponent[onick[1]]["id"]' :nick = 'onick[1]'></vpinfo>
          </td>
        </tr>
        <tr>
          <td rowspan="2">
            <vpinfo v-if = 'onick.length > 0' :id= 'opponent[onick[0]]["id"]' :nick = 'onick[0]'></vpinfo>
          </td>
          <td>
            <Table :key = 'refresh'></Table>
          </td>
          <td rowspan="2">
            <vpinfo v-if = 'onick.length > 2' :id= 'opponent[onick[2]]["id"]' :nick = 'onick[2]'></vpinfo>
          </td>
        </tr>
        <tr>
          <td>
            <vpinfo :id= 'player["id"]' :nick = 'gamernick'></vpinfo>
          </td>
        </tr>
      </table>
      <div v-if = "turn == player['id']">
        <div v-if= "createSwap" >
          <srack @cancel = 'cancel' @swapped = 'swapped'></srack>
        </div>
        <div v-else>
          <botton @clicked = 'refreshtable' @swapb = 'swap'></botton>
        </div>
      </div>
      <div v-else-if="turn == 5">
        <span>PROBE?</span>
        <button>YES</button>
        <button>NO</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Table from './Table.vue'
import store from '../store/index'
import vpinfo from './vpinfo'
import botton from './bottons'
import srack from './srack'
export default {
  name: 'Room',
  components: {
    Table,
    vpinfo,
    botton,
    srack
  },
  computed: {
    turn () {
      return store.getters.getturn
    }
  },
  data () {
    return {
      player: store.state.player,
      onick: Object.keys(store.state.opponent),
      opponent: store.state.opponent,
      refresh: 0,
      createSwap: false,
      gamernick: store.state.gamernick
    }
  },
  methods: {
    refreshtable () {
      store.dispatch('cleartiles')
      this.refresh++
    },
    swap () {
      this.createSwap = true
    },
    cancel () {
      store.dispatch('clearswaptile')
      this.createSwap = false
      this.refresh++
    },
    swapped () {
      this.createSwap = false
    }
  }
}
</script>

<style scoped>
  .game td{
    height: 5rem;
    width: 5rem;
    border: 2px ;
    text-align: center;
    font-size: 2rem;
    align-items: center;
    /*padding: 2px;*/
  }
  .game{
    width: 100%;
    height: 100%;
    margin: auto;
    /* background-color: rgb(157, 157, 219); */
    align-items: center;
    vertical-align: center;
  }
  .main{
    width: 920px;
    height:920px;
    margin: 5px;
    background-color: rgb(157, 157, 219);
    align-items: center;
    border: 3px solid black;
  }
</style>

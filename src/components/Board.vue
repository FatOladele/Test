<template>
  <div class= "board">
    <table>
      <tr v-for= "(value, key) in boardcode.rows" :key = "key">
        <td v-for= "j in boardcode.columns" :key = "j" :id= "key + j" >
          <bletter v-if = 'letonboard[value - 1][j -1] !== 0' :letcode = "'L' + letonboard[value - 1][j -1]['lp']" :letcol = "colourcode[letonboard[value - 1][j -1]['pl']]" >
            <!-- nothing -->
          </bletter>
          <bslot v-else :bid ="'B' + key + j" >
          </bslot>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import bslot from './bslot.vue'
import store from '../store/index'
import bletter from './bletter.vue'
export default {
  name: 'Board',
  components: {
    bslot,
    bletter
  },
  computed: {
    letonboard () {
      return store.getters.getboard
    }
  },
  data () {
    return {
      boardcode: {
        rows: {
          A: 1,
          B: 2,
          C: 3,
          D: 4,
          E: 5,
          F: 6,
          G: 7,
          H: 8,
          I: 9,
          J: 10,
          K: 11,
          L: 12,
          M: 13,
          N: 14,
          O: 15
        },
        columns: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
      },
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r',
        5: 'p'
      }
      // letonboard: store.getters.getboard
    }
  },
  method: {
  }
}
</script>

<style  scoped>
  table {
    table-layout: fixed ;
    width: 100% ;
    height: 100%;
    border-collapse: collapse ;
    border: 1px black solid ;
    margin-top: 2px solid black;
    margin-bottom: 2px solid black;
  }
  .board{
    height: 600px;
    width: 600px;
    background: black;
  }
  .board td {
    display: inline-block;
    height: 35px;
    width: 35px;
    background-color: burlywood;
    border: 1px solid black;
    text-align: center;
    font-size: 1rem;
    /*padding: 2px;*/
  }
  .board td bslot {
    display: inline-block;
  }
  #B6, #B10, #F2, #F6, #F10, #F14, #J2, #J6, #J10, #J14, #N6, #N10 {
    background-color: purple;
  }
  #A4, #A12, #C7, #C9, #D1, #D8, #D15, #G3, #G7, #G9, #G13, #H4, #H12, #I3, #I7, #I9, #I13, #L1, #L8, #L15, #M7, #M9, #O4, #O12{
    background-color: lightskyblue;
  }
  #A1, #A8, #A15, #H1, #H15, #O1, #O8, #O15{
    background-color: orangered;
  }
  #B2, #C3, #D4, #E5, #H8, #K11, #L12, #M13, #N14, #B14, #C13, #D12, #E11, #K5, #L4, #M3, #N2{
    background-color: orange;
  }
  #H8 {
    background-image: url("../assets/Alphabet/ST.png");
    background-repeat: no-repeat;
  }
</style>

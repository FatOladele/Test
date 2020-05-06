<template>
  <div>
    <div class = "pwords">
      <h2> WORDS PLAYED</h2>
      <table class = "maint">
        <tr v-for= "i in wordsplayed" :key = "i.id" :class = 'colourcode[i.id]' >
          <td>
            <table>
              <tr v-for= "w in i.words" :key= "'r' + w[0][0]">
                <td>
                  <bletter v-if = 'w.length > 0' :letcode = "'L' + w[0]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 1' :letcode = "'L' + w[1]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 2' :letcode = "'L' + w[2]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 3' :letcode = "'L' + w[3]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 4' :letcode = "'L' + w[4]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 5' :letcode = "'L' + w[5]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 6' :letcode = "'L' + w[6]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
                <td>
                  <bletter v-if = 'w.length > 7' :letcode = "'L' + w[7]" :letcol = "colourcode[i.id]" >
                  <!-- nothing -->
                  </bletter>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
    <div>
      <div>
        <table class = "maint">
          <tr v-for= "o in opponents" :key= "'tr' + o.id" :class = "colourcode[o.id]">
            <td>
              <span>
                Score: {{o.score}}
              </span>
              <span v-if= "o.id === turn" >
                Timer: {{cdt}}
              </span>
              <span v-else>
                Timer: {{o.time}}
              </span>
            </td>
            <br>
          </tr>
        </table>
      </div>
    </div>
    <div v-if="isPlayer === 'player'" :class = "colourcode[player.id]">
      <span>
        Score: {{player.score}}
      </span>
      <span v-if= "player.id === turn" >
        Timer: {{cdt}}
      </span>
      <span v-else>
        Timer: {{player.time}}
      </span>
    </div>
    <div :key ='bag'>
      Tiles left: {{cbag}}
    </div>
    <div class = "alog">
      <h3>ACTIVITIES</h3>
      <table>
        <tr v-for= "i in activities.length" :key = 'i' >
          <td>
            {{activities[i-1]}}
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import store from '../store'
import bletter from './bletter.vue'
export default {
  name: 'info',
  components: {
    bletter
  },
  computed: {
    cbag () {
      return store.getters.baggetters
    },
    activities () {
      return store.getters.actgetters
    },
    wordsplayed () {
      return store.getters.getwords
    }
  },
  data () {
    return {
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      },
      opponents: store.state.opponent,
      player: store.state.player,
      cbt: store.getters.getPtime,
      cdt: 580,
      turn: store.state.turn,
      isPlayer: store.state.gtype
    }
  }
}
</script>

<style scoped>
.pwords, .alog{
  margin: 10px;
  min-height: 400px;
  max-height: 450px;
  overflow-y: auto;
  padding: 5px;
  background-color: azure;
}
.alog tr{
  width: 100%;
}
h2{
  text-decoration-color: black;
  padding: 3px;
  margin: 2px;
}
h3{
  text-decoration-color: black;
  padding: 3px;
  margin: 2px;
}
.pwords tr{
  padding: 3px solid red;
  width: 100%;
}
.y{
  background-color: rgb(245, 245, 160)
}
.b{
  background-color: rgb(179, 179, 248)
}
.g{
  background-color: rgb(168, 253, 168)
}
.r{
  background-color: rgb(255, 163, 163)
}
span{
  padding: 3px;
  margin-bottom: 10px;
}
.maint{
  width: 90%;
  margin: 10px;
}
table td{
  margin: 10px;
}
div table tr{
  border: 10px;
}
</style>

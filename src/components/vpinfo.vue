<template>
  <div :class = 'colourcode[id]'>
    <table>
      <tr>
        <td>
          <P>{{nickn}}</P>
          <P>({{id}})</P>
          <div v-if = "turn === id">
            <p v-if = "id === pid">Your Turn</p>
            <p v-if = "id !== pid">Thinking...</p>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import store from '../store/index'
export default {
  props: ['id', 'nick'],
  data () {
    return {
      colourcode: {
        1: 'y',
        2: 'g',
        3: 'b',
        4: 'r'
      },
      pid: store.state.player.id,
      nickn: this.nick,
      turn: store.state.turn
    }
  }
}
</script>

<style scoped>
div{
  width: 100px;
  align-items: center;
  vertical-align: middle;
  align-self: center;
  margin: auto;
}
table{
  table-layout: fixed;
  margin: auto auto;
  width: 100%;
}
td{
  margin: auto auto;
}
p {
  padding: 0;
  margin: 5px;
  font-size: 15px;
}
.y td{
  background-color: yellow;
}
.y table{
  background-color: yellow;
}
.b td{
  background-color: blue;
}
.b table{
  background-color: blue;
}
.g td{
  background-color: green;
}
.g table{
  background-color: green;
}
.r td{
  background-color: red;
}
.r table{
  background-color: red;
}
</style>

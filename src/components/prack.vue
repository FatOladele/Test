<template>
  <div :class = '[ col, "prack"]'>
    <table>
      <tr>
        <td>
          <rslot id ="slot-1">
            <letter id = "letter-1" v-if ="letter.length > 0" :letcode = "'L' + letter[0]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-2">
            <letter id = "letter-2" v-if ="letter.length > 1" :letcode = "'L' + letter[1]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-3">
            <letter id = "letter-3" v-if ="letter.length > 2" :letcode = "'L' + letter[2]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-4">
            <letter id = "letter-4" v-if ="letter.length > 3" :letcode = "'L' + letter[3]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-5">
            <letter id = "letter-5" v-if ="letter.length > 4" :letcode = "'L' + letter[4]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-6">
            <!-- nothing -->
            <letter id = "letter-6" v-if ="letter.length > 5" :letcode = "'L' + letter[5]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
        <td>
          <rslot id ="slot-7">
            <letter id = "letter-7" v-if ="letter.length > 6" :letcode = "'L' + letter[6]" draggable="true" >
              <!-- nothing -->
            </letter>
          </rslot>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import rslot from './rslot.vue'
import letter from './letter.vue'
import store from '../store/index'
export default {
  props: ['col'],
  name: 'prack',
  computed: {
    letter () {
      return store.state.rack
    }
  },
  data () {
    return {
      letters: this.letter
    }
  },
  components: {
    rslot,
    letter
  }
}
</script>

<style scoped>
div{
  max-width: 100%;
  max-height: 100%;
  align-items: center;
}
table{
  table-layout: fixed;
  margin: auto auto;
  height: 40px;
  width: 280px;
}
td{
  height:36px;
  width: 36px;
  margin: auto auto;
}
.y td{
  background-color: yellow;
}
.y table{
  background-color: rgb(179, 179, 14);
}
.b td{
  background-color: blue;
}
.b table{
  background-color: rgb(13, 13, 194);
}
.g td{
  background-color: green;
}
.g table{
  background-color: rgb(9, 102, 9);
}
.r td{
  background-color: red;
}
.r table{
  background-color: rgb(201, 14, 14);
}
</style>

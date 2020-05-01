<template>
  <div :class = '[ col, "prack"]'>
    <div>
      <h3>LETTERS TO SWAP</h3>
    </div>
    <table>
      <tr>
        <td>
          <sslot sid ="sslot-1">
          </sslot>
        </td>
        <td>
          <sslot sid ="sslot-2">
          </sslot>
        </td>
        <td>
          <sslot sid ="sslot-3">
          </sslot>
        </td>
        <td>
          <sslot sid ="sslot-4">
          </sslot>
        </td>
        <td>
          <sslot sid ="sslot-5">
          </sslot>
        </td>
        <td>
          <sslot sid ="sslot-6">
          </sslot>
        </td>
        <td>
          <sslot id ="sslot-7">
          </sslot>
        </td>
      </tr>
    </table>
    <div>
      <button @click="swapped">SWAP</button>
    </div>
    <div>
      <button @click="cancel">CANCEL</button>
    </div>
  </div>
</template>

<script>
import sslot from './sslot.vue'
import store from '../store/index'
export default {
  props: ['col'],
  name: 'srack',
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
    sslot
  },
  methods: {
    cancel () {
      this.$emit('cancel')
    },
    swapped () {
      this.$emit('swapped')
    }
  }
}
</script>

<style scoped>
div{
  max-width: 100%;
  max-height: 100%;
  align-items: center;
  display: inline-flex;
  margin-left: 10px
}
table{
  table-layout: fixed;
  margin: auto auto;
  height: 40px;
  width: 280px;
  background-color: black
}
h3 {
  padding: 0px;
  margin: 0px;
  margin-right: 10px
}
td{
  height:36px;
  width: 36px;
  margin: auto auto;
  background-color: brown;
}
</style>

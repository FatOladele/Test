<template>
  <div>
    <button @click="emitevent"> emit </button>
    <p>{{response}}</p>
    <p>{{message}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'test',
  data () {
    return {
      message: 0,
      response: 'Server yet to respond'
    }
  },
  methods: {
    dragmousedown (e) {
      if (this.dragging === false) {
        this.pos3 = e.clientX
        this.pos4 = e.clientY
        this.offx = this.pos3 - this.pos1
        this.offy = this.pos4 - this.pos2
      }
      this.dragging = true
    },
    drag (e) {
      if (this.dragging === true) {
        // const offx = this.pos3 + this.pos1
        // const offy = this.pos4 + this.pos2
        this.pos1 = e.clientX - this.offx
        this.pos2 = e.clientY - this.offy
        this.leftpx = this.pos1 + 'px'
        this.toppx = this.pos2 + 'px'
      }
    },
    stopdrag () {
      // if (this.dragging === true) {
      //   this.offx = 0
      //   this.offy = 0
      // }
      this.dragging = false
      console.log('dragstop')
    },
    getMessage () {
      const path = 'http://localhost:5000/ping'
      axios.get(path).then((res) => {
        this.msg = res.data
      }).catch((error) => {
        console.log(error)
      })
    },
    emitevent () {
      this.$socket.emit('create', { size: 'normal', teams: 2, dictionary: 'Simple' })
      console.log('emmitted')
    }
  },
  created () {
    console.log('i got here')
    this.sockets.subscribe('after_connect', (data) => {
      this.response = data
      console.log(data)
    })
    this.sockets.subscribe('message', (data) => {
      this.message = this.message + 1
      console.log(data)
    })
  }
}
</script>

<style scoped>
  #mydiv {
    position: absolute;
    z-index: 9;
    background-color: #f1f1f1;
    border: 1px solid #d3d3d3;
    text-align: center;
  }

  #mydivheader {
    padding: 10px;
    cursor: move;
    z-index: 10;
    background-color: #2196F3;
    color: #fff;
  }
  #maindiv {
    width: 1000px;
    height:1000px;
  }
</style>

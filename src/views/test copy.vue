<template>
  <div>
    <!-- Draggable DIV -->
    <div id = "maindiv"  @mouseup.prevent="stopdrag" @mousemove="drag($event)">
      <div id="mydiv"  @mousedown.prevent="dragmousedown($event)" :style = "{top: toppx, left: leftpx}">
        <!-- Include a header DIV with the same name as the draggable DIV, followed by "header" -->
        <div id="mydivheader">Click here to move</div>
        <p>Move</p>
        <p>this</p>
        <p>DIV</p>
        <p>{{pos1}}</p>
        <p>{{toppx}}</p>
        <p>{{leftpx}}</p>
      </div>
    </div>
    <div>
      <!-- <button @click="connectit"> connect</button> -->
    </div>
    <div>
      <p>{{msg}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'test',
  data () {
    return {
      pos1: 0,
      pos2: 0,
      pos3: 0,
      pos4: 0,
      offx: 0,
      offy: 0,
      dragging: false,
      toppx: '0px',
      leftpx: '0px',
      msg: ''
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
    }
  },
  created () {
    console.log('i got here')
    this.getMessage()
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

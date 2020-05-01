<template>
  <div v-if = '!isConnected'>
    Can not Extablish a Connection
  </div>
</template>

<script>
export default {
  name: 'cfooter',
  data () {
    return {
      isConnected: false
    }
  },
  sockets: {
    connect: function () {
      this.isConnected = true
    },
    disconnect: function () {
      this.isConnected = false
    }
  }
}
</script>

<style scoped>
div{
  background-color: red;
  width: 80%;
  margin: auto
}
</style>

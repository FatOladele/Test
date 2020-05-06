<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>|
      <router-link to = "/test">test</router-link>
    </div> -->
    <div>
      <h4>Welcome {{gamernick}}</h4>
    </div>
    <router-view/>
    <footer>
      <cfooter></cfooter>
    </footer>
  </div>
</template>

<script>
import cfooter from './components/cfooter.vue'
import store from './store/index'
export default {
  components: {
    cfooter
  },
  computed: {
    gamernick () {
      return store.state.gamernick
    },
    isConnected () {
      return store.state.connection
    }
  },
  mounted () {
    // var externalScript = document.createElement('script')
    // externalScript.setAttribute('src', './src/assets/js/DragDropTouch.js')
    // document.head.appendChild(externalScript)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

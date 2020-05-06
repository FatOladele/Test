<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <setting/>
  </div>
</template>

<script>
// @ is an alias to /src
import setting from '@/components/setting.vue'
import store from '../store/index'
export default {
  name: 'Home',
  components: {
    setting
  },
  data () {
    return {
      gamerNick: ''
    }
  },
  created () {
    store.dispatch('setDefaultState')
  }
}
</script>

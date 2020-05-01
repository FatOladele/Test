import VueSocketio from 'vue-socket.io'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.use(new VueSocketio({
  debug: true,
  connection: 'http://127.0.0.1:5000',
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
}))
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

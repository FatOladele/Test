import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    gamernick: 'Gamer',
    rack: [],
    // boardl: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, { pl: 3, lp: 112 }, { pl: 4, lp: 115 }, { pl: 4, lp: 114 }, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, { pl: 1, lp: 112 }, 0, { pl: 3, lp: 115 }, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, { pl: 2, lp: 116 }, { pl: 1, lp: 111 }, { pl: 2, lp: 114 }, { pl: 2, lp: 115 }, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, { pl: 1, lp: 114 }, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    // opponent: [{ id: 2, nick: 'Paul', score: 0, timer: 600 }, { id: 3, nick: 'Omo Wobe', score: 0, timer: 600 }, { id: 4, nick: 'Computer', score: 0, timer: 600 }],
    boardl: [],
    // opponent: { paul: { id: 2, score: 0, time: 500 }, omowobe: { id: 3, score: 0, time: 500 }, Computer: { id: 4, score: 0, time: 500 } },
    // player: { id: 1, score: 0, timer: 600 },
    opponent: {},
    player: {},
    turn: 1,
    tonboard: {},
    bag: 0,
    playedWords: [],
    activities: [],
    swaptiles: [],
    connection: false,
    slot: {},
    gameId: '',
    settings: {},
    isHost: false
  },
  getters: {
    noT (state) { return Object.keys(state.tonboard).length },
    getPtime  (state) {
      var ptime = 0
      for (var i in state.opponent) {
        if (state.opponent[i].id === state.turn) {
          ptime = state.opponent[i].timer - 10
        }
        if (state.player.id === state.turn) {
          ptime = state.player.timer - 10
        }
      }
      return ptime
    },
    baggetters (state) {
      console.log(state.bag)
      return state.bag
    },
    getturn (state) {
      return state.turn
    }
  },
  mutations: {
    SOCKET_connect (state) {
      state.connection = true
    },
    SOCKET_connected (state, data) {
      state.gamernick = data.gamernick
      console.log(data.gamernick)
    },
    connectionlost (state) {
      state.connection = false
    },
    addtonboard (state, letter) {
      state.tonboard[letter[0]] = letter[1]
    },
    removetile (state, slot) {
      delete state.tonboard[slot]
    },
    updateboard (state, board) {
      state.boardl = board
    },
    updatebag (state, bag) {
      state.bag = bag
    },
    updateturn (state, turn) {
      state.turn = turn
    },
    setplayer (state, player) {
      state.player = player
    },
    setopponent (state, opponent) {
      state.opponent = opponent
    },
    cleartile (state) {
      state.tonboard = {}
    },
    swaptile (state, tile) {
      state.swaptiles = [...state.swaptiles, tile]
    },
    removeswap (state, tile) {
      const idx = state.swaptiles.findIndex(p => p === tile)
      state.swaptiles.splice(idx, 1)
    },
    clearswap (state) {
      state.swaptiles = []
    },
    gamerid (state, gamerId) {
      state.gamernick = gamerId
    },
    mutgsetting (state, settings) {
      state.settings = settings
    },
    setgameid (state, gameid) {
      state.gameId = gameid
    },
    updateslot (state, slot) {
      state.slot = slot
    },
    sethost (state, bool) {
      state.isHost = bool
    },
    setDefaultState (state) {
      state.isHost = false
      state.rack = []
      state.boardl = []
      state.opponent = []
      state.player = {}
      state.turn = 0
      state.tonboard = {}
      state.bag = 0
      state.playedWords = []
      state.activities = []
      state.swaptiles = []
      state.slot = {}
      state.gameId = ''
      state.settings = {}
      state.isHost = false
    },
    updaterack (slot, rack) {
      slot.rack = rack
    }
  },
  actions: {
    addtonboardaction (context, letter) {
      context.commit('addtonboard', letter)
    },
    removetilea (context, slot) {
      context.commit('removetile', slot)
    },
    cleartiles (context) {
      context.commit('cleartile')
    },
    addswaptile (context, tile) {
      context.commit('swaptile', tile)
    },
    removeswaptile (context, lclass) {
      context.commit('removeswap', lclass)
    },
    clearswaptile (context) {
      context.commit('clearswap')
    },
    addgamerId (context, gamerId) {
      context.commit('gamerid', gamerId)
    },
    SOCKET_update_room (context, data) {
      if (Object.keys(this.state.settings).length === 0) {
        const settings = { time: data.roomdata.time, rules: data.roomdata.rules, creator: data.roomdata.creator }
        if (data.roomdata.creator !== this.state.gamernick) {
          context.commit('sethost', false)
        } else {
          context.commit('sethost', true)
        }
        context.commit('mutgsetting', settings)
      }
      if (this.state.gameId === '') {
        const gameid = data.gameid
        context.commit('setgameid', gameid)
      }
      const slot = data.roomdata.slot
      context.commit('updateslot', slot)
      router.push({ name: 'game' })
    },
    SOCKET_left_room (context) {
      alert('You have left the game')
      context.commit('setDefaultState')
      router.push({ name: 'Home' })
    },
    SOCKET_error (context, data) {
      alert(data.error)
    },
    setDefaultState (context) {
      context.commit('setDefaultState')
    },
    SOCKET_disconnect (context) {
      context.commit('setDefaultState')
      context.commit('connectionlost')
      router.push({ name: 'Home' })
    },
    SOCKET_game_start (context, data) {
      // const bag = data.bag
      var players = data.players
      const turn = data.turn
      const board = data.board
      const player = players[this.state.gamernick]
      delete players[this.state.gamernick]
      const opponent = players
      context.commit('updateboard', board)
      // context.commit('updatebag', bag)
      context.commit('updateturn', turn)
      context.commit('setplayer', player)
      context.commit('setopponent', opponent)
      const payload = { id: this.state.gameId, rack: this.state.rack, gamer: this.state.gamernick }
      console.log(payload)
      const path = 'http://localhost:5000/api/refillrack'
      axios.post(path, payload).then((res) => {
        if (res.data.status === 'failed') {
          alert(res.data.msg)
        } else {
          const rack = res.data.rack
          context.commit('updaterack', rack)
          this._vm.$socket.emit('updated_rack', { room: this.state.gameId })
          router.push({ name: 'play' })
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    SOCKET_update_bag (context, data) {
      context.commit('updatebag', data.bag)
      console.log(this.state.bag)
    }
  },
  modules: {
  }
})

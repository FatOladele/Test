import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    gamernick: 'Gamer',
    rack: [],
    orack: [],
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
    isHost: false,
    selected: {},
    blanks: false,
    bpos: [],
    endgame: false,
    enddata: [],
    gtype: 'none',
    observers: [],
    oa: false
  },
  getters: {
    getselect (state) {
      return state.selected
    },
    getend (state) {
      return state.endgame
    },
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
    },
    getboard (state) {
      return state.boardl
    },
    actgetters (state) {
      return state.activities
    },
    getwords (state) {
      return state.playedWords
    },
    getrack (state) {
      return state.rack
    },
    bsgetter (state) {
      return state.blanks
    },
    getenddata (state) {
      return state.enddata
    },
    getobserve (state) {
      return state.observers
    }
  },
  mutations: {
    SOCKET_connect (state) {
      state.connection = true
    },
    selecttile (state, ids) {
      state.selected = ids
    },
    SOCKET_connected (state, data) {
      state.gamernick = data.gamernick
      console.log(data.gamernick)
    },
    SOCKET_game_ended (state, data) {
      state.enddata = data
      state.endgame = true
    },
    connectionlost (state) {
      state.connection = false
    },
    gtype (state, type) {
      state.gtype = type
    },
    updateobservers (state, observers) {
      state.observers = observers
    },
    updateoa (state, oa) {
      state.oa = oa
    },
    addtonboard (state, letter) {
      state.tonboard[letter[0]] = letter[1]
    },
    exchangerack (state, rack) {
      state.rack = rack
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
    updateactivity (state, activity) {
      state.activities = [...activity, ...state.activities]
    },
    updateoppscore (state, player) {
      state.opponent[player[0]].score = parseInt(player[1]) + parseInt(state.opponent[player[0]].score)
    },
    updatepscore (state, score) {
      state.player.score = parseInt(score) + parseInt(state.player.score)
    },
    updateplayedwords (state, words) {
      state.playedWords = [words, ...state.playedWords]
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
      state.swaptiles = [tile, ...state.swaptiles]
    },
    removeswap (state, tile) {
      const idx = state.swaptiles.findIndex(p => p === tile)
      state.swaptiles.splice(idx, 1)
    },
    playtile (state) {
      state.orack = [...state.rack]
      for (var i in Object.values(state.tonboard)) {
        if (i > 200) {
          i = 200
        }
        const idx = state.rack.findIndex(p => p === i)
        state.rack.splice(idx, 1)
      }
      state.tonboard = {}
    },
    clearswap (state) {
      console.log('I am here 2')
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
    updaterack (state, rack) {
      state.rack = rack
    },
    revertrack (state) {
      state.rack = [...state.orack]
      state.orack = []
    },
    addblanktile (state, lobject) {
      state.blanks = true
      state.bpos = lobject
    },
    removeblanktile (state) {
      state.blanks = false
      state.bpos = []
    }
  },
  actions: {
    addtonboardaction (context, letter) {
      context.commit('addtonboard', letter)
    },
    swapped (context, rack) {
      context.commit('clearswap')
      context.commit('exchangerack', rack)
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
        const oa = data.roomdata.observe
        context.commit('updateoa', oa)
      }
      if (this.state.gameId === '') {
        const gameid = data.gameid
        context.commit('setgameid', gameid)
      }
      const slot = data.roomdata.slot
      context.commit('updateslot', slot)
      if (router.currentRoute.name === 'Home') {
        router.push({ name: 'game' })
      }
      if (this.state.oa) {
        const observers = data.roomdata.olist
        context.commit('updateobservers', observers)
      }
    },
    SOCKET_left_room (context) {
      alert('You have left the game')
      router.push({ name: 'Home' })
      context.commit('setDefaultState')
    },
    SOCKET_error (context, data) {
      alert(data.error)
    },
    setDefaultState (context) {
      context.commit('setDefaultState')
    },
    SOCKET_disconnect (context) {
      router.push({ name: 'Home' })
      context.commit('setDefaultState')
      context.commit('connectionlost')
    },
    SOCKET_game_start (context, data) {
      // const bag = data.bag
      var players = data.players
      const turn = data.turn
      const board = data.board
      var player = {}
      if (this.state.gtype === 'player') {
        player = players[this.state.gamernick]
        delete players[this.state.gamernick]
      } else {
        player = { id: 7 }
      }
      const opponent = players
      console.log(opponent)
      context.commit('updateboard', board)
      // context.commit('updatebag', bag)
      context.commit('updateturn', turn)
      context.commit('setplayer', player)
      context.commit('setopponent', opponent)
      if (this.state.gtype === 'player') {
        const payload = { id: this.state.gameId, rack: this.state.rack, gamer: this.state.gamernick }
        const path = this._vm.$myhost + '/api/refillrack'
        axios.post(path, payload).then((res) => {
          if (res.data.status === 'failed') {
            alert(res.data.msg)
          } else {
            const rack = res.data.rack
            context.commit('updaterack', rack)
            this._vm.$socket.emit('updated_rack', { room: this.state.gameId })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
      router.push({ name: 'play' })
    },
    SOCKET_update_bag (context, data) {
      context.commit('updatebag', data.bag)
    },
    SOCKET_pass_swap (context, data) {
      const activity = data.activity
      context.commit('updateactivity', activity)
      const turn = data.turn
      context.commit('updateturn', turn)
    },
    playtilea (context) {
      context.commit('playtile')
      context.commit('updateturn', 0)
    },
    SOCKET_pre_play (context, data) {
      const board = data.board
      const gamer = data.gamer
      context.commit('updateboard', board)
      if (gamer !== this.state.gamernick && this.state.gtype === 'player') {
        context.commit('updateturn', 5)
      }
    },
    proberes (context) {
      context.commit('updateturn', 0)
    },
    SOCKET_post_play (context, data) {
      const player = data.gamer
      const turn = data.turn
      context.commit('updateturn', turn)
      const board = data.board
      context.commit('updateboard', board)
      const activity = data.activity
      context.commit('updateactivity', activity)
      const score = data.score
      const words = data.pwords
      const stat = data.stat
      if (stat === 't') {
        if (player !== this.state.gamernick) {
          const pw = { id: this.state.opponent[player].id, words: words }
          context.commit('updateplayedwords', pw)
          context.commit('updateoppscore', [player, score])
        } else {
          const pw = { id: this.state.player.id, words: words }
          context.commit('updateplayedwords', pw)
          context.commit('updatepscore', score)
          const payload = { id: this.state.gameId, rack: this.state.rack, gamer: this.state.gamernick }
          const path = this._vm.$myhost + '/api/refillrack'
          axios.post(path, payload).then((res) => {
            if (res.data.status === 'failed') {
              alert(res.data.msg)
            } else {
              const rack = res.data.rack
              console.log(rack)
              context.commit('updaterack', rack)
              this._vm.$socket.emit('updated_rack', { room: this.state.gameId })
            }
          }).catch((error) => {
            console.log(error)
          })
        }
      } else {
        if (player === this.state.gamernick) {
          context.commit('revertrack')
        }
      }
      if ((parseInt(turn) === parseInt(this.state.player.id)) && (this.state.bag === 0) && (this.state.rack.length === 0)) {
        console.log('time to end the game')
        this._vm.$socket.emit('end_game', { room: this.state.gameId })
      }
    },
    selectedtile (context, ids) {
      context.commit('selecttile', ids)
    },
    addblank (context, tobject) {
      context.commit('addblanktile', tobject)
    },
    removeblank (context) {
      context.commit('removeblanktile')
    },
    SOCKET_pre_end () {
      if (this.state.gtype === 'player') {
        const tilesleft = this.state.rack
        this._vm.$socket.emit('my_tiles', { gamer: this.state.gamernick, room: this.state.gameId, rack: tilesleft })
      }
    },
    setgtype (context, type) {
      context.commit('gtype', type)
    }
  },
  modules: {
  }
})

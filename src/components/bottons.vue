<template>
  <div>
    <div>
      <Span>
        <button @click.prevent = 'play'>
          PLAY
        </button>
      </Span>
      <Span>
        <button @click.prevent = "toswap" :disabled = 'allowswap' >
          SWAP
        </button>
      </Span>
      <Span>
        <button >
          PASS
        </button>
      </Span>
      <Span>
        <button @click.prevent="onClear" >
          CLEAR
        </button>
      </Span>
    </div>
    <div v-if = "msg !== ''"> {{msg}} </div>
    <div v-if = "playedwords.length !== 0">
      <p v-for = "i in playedwords.length" :key ='i' >{{playedwords[i - 1]}}</p>
    </div>
  </div>
</template>

<script>
import store from '../store'
import axios from 'axios'
export default {
  computed: {
    playcheck () {
      return store.getters.noT
    },
    allowswap () {
      if (store.state.bag > 10) {
        return false
      } else {
        return true
      }
    }
  },
  data () {
    return {
      msg: '',
      playedwords: [],
      pwt: store.getters.noT,
      played: 'disabled',
      bag: store.state.bag
    }
  },
  methods: {
    play () {
      console.log(store.state.tonboard)
      const payload = { board: store.state.boardl, tiles: store.state.tonboard }
      const path = 'http://localhost:5000/api/played'
      axios.post(path, payload).then((res) => {
        if (res.data.status === 'failed') {
          this.msg = res.data.msg
        } else {
          this.msg = 'You Played'
          this.playedwords = res.data.words
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    onClear (event) {
      this.$emit('clicked')
    },
    toswap () {
      this.$emit('swapb')
    }
  }
}
</script>

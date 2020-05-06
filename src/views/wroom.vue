<template>
  <div>
    <div class = 'main'>
      <div v-if="isHost">
        Click slot to Toggle between Human, Computer, and None
      </div>
      <div>
        <span>GAME ID: {{gameId}}</span><span>TIME: {{setting['time']}}Seconds</span><span>RULES: {{setting['rules']}}</span><span v-if="oa"> OBSERVERS: Allowed</span><span v-else> OBSERVERS: Not Allowed</span>
      </div>
      <div class = 'mbox' >
        <div class = 'boxi'>
          <div>
            <button class = 'pbtn y' disabled = 'disabled'>
              <div>
                Slot 1
              </div>
              <div v-if="isHost">
                You
              </div>
              <div>
                Host
              </div>
            </button>
          </div>
          <div class = 'prac y'>
            <h4 v-if="slot['slot1']['nick']=== gamerNick">YOU</h4>
            <h4 v-else-if="slot['slot1']['nick']!== ''">{{slot['slot1']['nick']}}</h4>
            <h4 v-else> Waiting for player</h4>
          </div>
        </div>
        <div class = 'boxi'>
          <div>
            <button @click.prevent = "stoggle('slot2')" :disabled = "!isHost||(slot['slot2']['nick']!== '' && slot['slot2']['type']=== 'Human')" class = 'pbtn g'>
              <div>
                Slot 2
              </div>
              <div v-if="slot['slot2']['nick']!== gamerNick">
                <div>
                  {{slot['slot2']['type']}}
                </div>
                <div>
                  {{slot['slot2']['status']}}
                </div>
              </div>
              <div v-else>
                <div>{{isReady}}</div>
              </div>
            </button>
          </div>
          <div class = 'prac g'>
            <h4 v-if="slot['slot2']['nick']=== gamerNick">YOU</h4>
            <h4 v-else-if="slot['slot2']['nick']!== ''">{{slot['slot2']['nick']}}</h4>
            <h4 v-else> Waiting for player</h4>
          </div>
        </div>
        <div class = 'boxi'>
          <div>
            <button @click.prevent = "stoggle('slot3')" :disabled = "!isHost||(slot['slot3']['nick']!== '' && slot['slot3']['type']=== 'Human')" class = 'pbtn b'>
              <div>
                Slot 3
              </div>
              <div v-if="slot['slot3']['nick']!== gamerNick">
                <div>
                  {{slot['slot3']['type']}}
                </div>
                <div>
                  {{slot['slot3']['status']}}
                </div>
              </div>
              <div v-else>
                <div v-if='isReady'>Ready</div>
                <div V-else>Click Ready!</div>
              </div>
            </button>
          </div>
          <div class = 'prac b'>
            <h4 v-if="slot['slot3']['nick']=== gamerNick">YOU</h4>
            <h4 v-else-if="slot['slot3']['nick']!== ''">{{slot['slot3']['nick']}}</h4>
            <h4 v-else> Waiting for player</h4>
          </div>
        </div>
        <div class = 'boxi'>
          <div>
            <button @click.prevent = "stoggle('slot4')" :disabled = "!isHost||(slot['slot4']['nick']!== '' && slot['slot4']['type']=== 'Human')" class = 'pbtn r'>
              <div>
                Slot 4
              </div>
              <div v-if="slot['slot4']['nick']!== gamerNick">
                <div>
                  {{slot['slot4']['type']}}
                </div>
                <div>
                  {{slot['slot4']['status']}}
                </div>
              </div>
              <div v-else>
                <div v-if='isReady'>Ready</div>
                <div V-else>Click Ready!</div>
              </div>
            </button>
          </div>
          <div class = 'prac r'>
            <h4 v-if="slot['slot4']['nick']=== gamerNick">YOU</h4>
            <h4 v-else-if="slot['slot4']['nick']!== ''">{{slot['slot4']['nick']}}</h4>
            <h4 v-else> Waiting for player</h4>
          </div>
        </div>
      </div>
      <div v-if="isHost">
        <button @click="leaveroom">Cancel Game</button>
        <button @click='startgame'>Start game</button>
      </div>
      <div v-else>
        <button @click="leaveroom">Leave Game</button>
        <button v-if="isReady !== 'Ready' && isPlayer==='player'" @click = 'playerready'>Ready</button>
      </div>
    </div>
    <br>
    <div class="observe">
      <observers/>
    </div>
  </div>
</template>

<script>
import store from '../store/index'
import observers from '@/components/observers.vue'
export default {
  name: 'wroom',
  components: {
    observers
  },
  computed: {
    slot () {
      const slot = store.state.slot
      return slot
    }
  },
  data () {
    return {
      isHost: store.state.isHost,
      gamerNick: store.state.gamernick,
      gameId: store.state.gameId,
      setting: store.state.settings,
      isReady: 'Click Ready',
      isPlayer: store.state.gtype,
      oa: store.state.oa
    }
  },
  created () {
  },
  methods: {
    stoggle: function (sslot) {
      const type = this.slot[sslot].type
      var newtype = {}
      if (type === 'Human') {
        newtype = { type: 'Computer', status: 'Ready', nick: 'Computer' }
      } else if (type === 'Computer') {
        newtype = { type: 'None', status: 'Closed', nick: 'Closed' }
      } else if (type === 'None') {
        newtype = { type: 'Human', status: 'Waiting', nick: '' }
      }
      const gdata = { room: store.state.gameId, slot: sslot, info: newtype }
      this.$socket.emit('toggle_slot', gdata)
    },
    leaveroom: function () {
      if (confirm('Are you sure you want to leave the room')) {
        const gdata = { room: store.state.gameId, gamerid: this.gamerNick }
        this.$socket.emit('leave_room', gdata)
      }
    },
    playerready () {
      this.isReady = 'Ready'
      const gdata = { room: store.state.gameId, gamerid: this.gamerNick }
      this.$socket.emit('p_ready', gdata)
    },
    startgame () {
      var pslot = store.state.slot
      var readySlot = ['slot1']
      var canStart = true
      Object.keys(pslot).forEach((key) => {
        if (pslot[key].nick === '') {
          alert('You must close all empty slot before starting the game')
          canStart = false
        }
        if (pslot[key].type === 'Computer') {
          alert('Computer not available yet')
          canStart = false
        }
        if (pslot[key].status === 'Not Ready') {
          alert('Can not start unit all players are ready')
          canStart = false
        }
        if (pslot[key].type === 'Human' && pslot[key].status === 'Ready') {
          readySlot = [...readySlot, key]
        }
      })
      if ((readySlot.length < 2) && canStart) {
        canStart = false
        alert('There must be at least TWO player')
      }
      if (canStart) {
        const gdata = { room: store.state.gameId, slot: readySlot }
        this.$socket.emit('start_game', gdata)
        console.log(readySlot)
      }
    }
  }
}
</script>

<style scoped>
*{
  margin: 10px;
}
.observe {
  padding: 10px;
  margin: auto;
  border: 10px;
}
.mbox{
  display: inline-flex;
  align-items: center;
  width: 800px;
  height: 350px;
  margin: auto;
}
.main{
  padding: 5px;
  background-color: rgba(134, 124, 124, 0.212);
  width: 1000px;
  max-height: 500px;
  margin: auto;
  display: block
}
.boxi{
  width: 25%;
}
.pbtn{
  width: 100px;
  height: 100px;
  cursor: pointer;
  border: none;
}
.prac{
  width: 150px;
  margin: auto;
  display: inline-block
}
.h4{
  margin: 5px;
  padding: 5px;
}
.y{
  background-color: yellow;
}
.b{
  background-color: blue;
}
.g{
  background-color: green
}
.r{
  background-color: red;
}
</style>

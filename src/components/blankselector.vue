<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <h1> Select a letter</h1>
      </header>
      <section class="modal-body">
        <table>
          <tr>
            <td id = 'L211' @click.stop @click.prevent="select"></td>
            <td id = 'L212' @click.stop @click.prevent="select"></td>
            <td id = 'L213' @click.stop @click.prevent="select"></td>
            <td id = 'L214' @click.stop @click.prevent="select"></td>
            <td id = 'L215' @click.stop @click.prevent="select"></td>
            <td id = 'L216' @click.stop @click.prevent="select"></td>
            <td id = 'L217' @click.stop @click.prevent="select"></td>
            <td id = 'L218' @click.stop @click.prevent="select"></td>
            <td id = 'L219' @click.stop @click.prevent="select"></td>
            <td id = 'L220' @click.stop @click.prevent="select"></td>
          </tr>
          <tr>
            <td id = 'L221' @click.stop @click.prevent="select"></td>
            <td id = 'L222' @click.stop @click.prevent="select"></td>
            <td id = 'L223' @click.stop @click.prevent="select"></td>
            <td id = 'L224' @click.stop @click.prevent="select"></td>
            <td id = 'L225' @click.stop @click.prevent="select"></td>
            <td id = 'L226' @click.stop @click.prevent="select"></td>
            <td id = 'L227' @click.stop @click.prevent="select"></td>
            <td id = 'L228' @click.stop @click.prevent="select"></td>
            <td id = 'L229' @click.stop @click.prevent="select"></td>
            <td id = 'L230' @click.stop @click.prevent="select"></td>
          </tr>
          <tr>
            <td id = 'L231' @click.stop @click.prevent="select"></td>
            <td id = 'L232' @click.stop @click.prevent="select"></td>
            <td id = 'L233' @click.stop @click.prevent="select"></td>
            <td id = 'L234' @click.stop @click.prevent="select"></td>
            <td id = 'L235' @click.stop @click.prevent="select"></td>
            <td id = 'L236' @click.stop @click.prevent="select"></td>
            <td id = 'L237' @click.stop @click.prevent="select"></td>
            <td id = 'L238' @click.stop @click.prevent="select"></td>
            <td id = 'L239' @click.stop @click.prevent="select"></td>
            <td id = 'L240' @click.stop @click.prevent="select"></td>
          </tr>
          <tr>
            <td id = 'L241' @click.stop @click.prevent="select"></td>
            <td id = 'L242' @click.stop @click.prevent="select"></td>
            <td id = 'L243' @click.stop @click.prevent="select"></td>
            <td id = 'L244' @click.stop @click.prevent="select"></td>
            <td id = 'L245' @click.stop @click.prevent="select"></td>
            <td id = 'L246' @click.stop @click.prevent="select"></td>
            <td id = 'L247' @click.stop @click.prevent="select"></td>
            <td id = 'L248' @click.stop @click.prevent="select"></td>
            <td id = 'L249' @click.stop @click.prevent="select"></td>
            <td id = 'L250' @click.stop></td>
          </tr>
        </table>
      </section>
    </div>
  </div>
</template>

<script>
import store from '../store/index'
export default {
  name: 'blankselector',
  methods: {
    select: e => {
      let lclass = e.target.id
      lclass = lclass.toString().substring(1)
      lclass = parseInt(lclass)
      const lobject = store.state.bpos
      const letter = document.getElementById(lobject[1])
      const lcl = e.target.id + ' letter'
      letter.classList = lcl
      store.dispatch('addtonboardaction', [lobject[0], lclass])
      store.dispatch('removeblank')
    }
  }
}
</script>

<style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }
  td {
    width: 32px;
    height: 32px;
    border: 3px solid black
  }
  #L211{
    background-image: url("../assets/Alphabet/211.jpg");
    background-repeat: no-repeat;
  }
  #L212{
    background-image: url("../assets/Alphabet/212.jpg");
    background-repeat: no-repeat;
  }
  #L213{
    background-image: url("../assets/Alphabet/213.jpg");
    background-repeat: no-repeat;
  }
  #L214{
    background-image: url("../assets/Alphabet/214.jpg");
    background-repeat: no-repeat;
  }
  #L215{
    background-image: url("../assets/Alphabet/215.jpg");
    background-repeat: no-repeat;
  }
  #L216{
    background-image: url("../assets/Alphabet/216.jpg");
    background-repeat: no-repeat;
  }
  #L217{
    background-image: url("../assets/Alphabet/217.jpg");
    background-repeat: no-repeat;
  }
  #L218{
    background-image: url("../assets/Alphabet/218.jpg");
    background-repeat: no-repeat;
  }
  #L219{
    background-image: url("../assets/Alphabet/219.jpg");
    background-repeat: no-repeat;
  }
  #L220{
    background-image: url("../assets/Alphabet/220.jpg");
    background-repeat: no-repeat;
  }
  #L221{
    background-image: url("../assets/Alphabet/221.jpg");
    background-repeat: no-repeat;
  }
  #L222{
    background-image: url("../assets/Alphabet/222.jpg");
    background-repeat: no-repeat;
  }
  #L223{
    background-image: url("../assets/Alphabet/223.jpg");
    background-repeat: no-repeat;
  }
  #L224{
    background-image: url("../assets/Alphabet/224.jpg");
    background-repeat: no-repeat;
  }
  #L225{
    background-image: url("../assets/Alphabet/225.jpg");
    background-repeat: no-repeat;
  }
  #L226{
    background-image: url("../assets/Alphabet/226.jpg");
    background-repeat: no-repeat;
  }
  #L227{
    background-image: url("../assets/Alphabet/227.jpg");
    background-repeat: no-repeat;
  }
  #L228{
    background-image: url("../assets/Alphabet/228.jpg");
    background-repeat: no-repeat;
  }
  #L229{
    background-image: url("../assets/Alphabet/229.jpg");
    background-repeat: no-repeat;
  }
  #L230{
    background-image: url("../assets/Alphabet/230.jpg");
    background-repeat: no-repeat;
  }
  #L231{
    background-image: url("../assets/Alphabet/231.jpg");
    background-repeat: no-repeat;
  }
  #L232{
    background-image: url("../assets/Alphabet/232.jpg");
    background-repeat: no-repeat;
  }
  #L233{
    background-image: url("../assets/Alphabet/233.jpg");
    background-repeat: no-repeat;
  }
  #L234{
    background-image: url("../assets/Alphabet/234.jpg");
    background-repeat: no-repeat;
  }
  #L235{
    background-image: url("../assets/Alphabet/235.jpg");
    background-repeat: no-repeat;
  }
  #L236{
    background-image: url("../assets/Alphabet/236.jpg");
    background-repeat: no-repeat;
  }
  #L237{
    background-image: url("../assets/Alphabet/237.jpg");
    background-repeat: no-repeat;
  }
  #L238{
    background-image: url("../assets/Alphabet/238.jpg");
    background-repeat: no-repeat;
  }
  #L239{
    background-image: url("../assets/Alphabet/239.jpg");
    background-repeat: no-repeat;
  }
  #L240{
    background-image: url("../assets/Alphabet/240.jpg");
    background-repeat: no-repeat;
  }
  #L241{
    background-image: url("../assets/Alphabet/241.jpg");
    background-repeat: no-repeat;
  }
  #L242{
    background-image: url("../assets/Alphabet/242.jpg");
    background-repeat: no-repeat;
  }
  #L243{
    background-image: url("../assets/Alphabet/243.jpg");
    background-repeat: no-repeat;
  }
  #L244{
    background-image: url("../assets/Alphabet/244.jpg");
    background-repeat: no-repeat;
  }
  #L245{
    background-image: url("../assets/Alphabet/245.jpg");
    background-repeat: no-repeat;
  }
  #L246{
    background-image: url("../assets/Alphabet/246.jpg");
    background-repeat: no-repeat;
  }
  #L247{
    background-image: url("../assets/Alphabet/247.jpg");
    background-repeat: no-repeat;
  }
  #L248{
    background-image: url("../assets/Alphabet/248.jpg");
    background-repeat: no-repeat;
  }
  #L249{
    background-image: url("../assets/Alphabet/249.jpg");
    background-repeat: no-repeat;
  }
</style>

<template>
  <div class= "board">
    <table :v-for= "i in board.rows">
      <tr :v-for= "j in board.columns">
        <td id={{i + j}}>
          {{i + j}}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Board',
  data () {
    return {
      board: {
        rows: ['A', 'B', 'C', ' D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0'],
        columns: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
      }
    }
  }
}
</script>

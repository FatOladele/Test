<template>
  <div :class = 'col'>
    <table>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
      <tr>
        <td>
          <!-- nothing -->
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: ['col'],
  data () {
    return {
      initialpos: 'a'
    }
  }
}
</script>

<style scoped>
div{
  width: 100%;
  height: 280px;
  vertical-align: middle;
}
table{
  table-layout: fixed;
  height: 280px;
  width: 40px;
}
td{
  height:40px;
  width: 40px;
}
.y td{
  background-color: yellow;
}
.y table{
  background-color: rgb(179, 179, 14);
}
.b td{
  background-color: blue;
}
.b table{
  background-color: rgb(13, 13, 194);
}
.g td{
  background-color: green;
}
.g table{
  background-color: rgb(9, 102, 9);
}
.r td{
  background-color: red;
}
.r table{
  background-color: rgb(201, 14, 14);
}
</style>

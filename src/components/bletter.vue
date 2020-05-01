<template>
  <div :class="[letcode, letcol, 'letter']" >
  <slot/>
  </div>
</template>

<script>
export default {
  props: ['letcode', 'letcol']
}
</script>

<style scoped>
  .letter{
    width: 31px;
    height: 31px;
    padding: 0;
    margin: auto;
    /* background-color: green; */
    display : inline-block;
  }
  .y{
    border: 3px solid yellow;
  }
  .b{
    border: 3px solid blue;
  }
  .g{
    border: 3px solid green;
  }
  .r{
    border: 3px solid red;
  }
  .p{
    border: 3px solid brown;
  }
  .L111{
    background-image: url("../assets/Alphabet/111.jpg");
    background-repeat: no-repeat;
  }
  .L112{
    background-image: url("../assets/Alphabet/112.jpg");
    background-repeat: no-repeat;
  }
  .L113{
    background-image: url("../assets/Alphabet/113.jpg");
    background-repeat: no-repeat;
  }
  .L114{
    background-image: url("../assets/Alphabet/114.jpg");
    background-repeat: no-repeat;
  }
  .L115{
    background-image: url("../assets/Alphabet/115.jpg");
    background-repeat: no-repeat;
  }
  .L116{
    background-image: url("../assets/Alphabet/116.jpg");
    background-repeat: no-repeat;
  }
  .L117{
    background-image: url("../assets/Alphabet/117.jpg");
    background-repeat: no-repeat;
  }
</style>

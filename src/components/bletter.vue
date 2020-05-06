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
  .L118{
    background-image: url("../assets/Alphabet/118.jpg");
    background-repeat: no-repeat;
  }
  .L119{
    background-image: url("../assets/Alphabet/119.jpg");
    background-repeat: no-repeat;
  }
  .L120{
    background-image: url("../assets/Alphabet/120.jpg");
    background-repeat: no-repeat;
  }
  .L121{
    background-image: url("../assets/Alphabet/121.jpg");
    background-repeat: no-repeat;
  }
  .L122{
    background-image: url("../assets/Alphabet/122.jpg");
    background-repeat: no-repeat;
  }
  .L123{
    background-image: url("../assets/Alphabet/123.jpg");
    background-repeat: no-repeat;
  }
  .L124{
    background-image: url("../assets/Alphabet/124.jpg");
    background-repeat: no-repeat;
  }
  .L125{
    background-image: url("../assets/Alphabet/125.jpg");
    background-repeat: no-repeat;
  }
  .L126{
    background-image: url("../assets/Alphabet/126.jpg");
    background-repeat: no-repeat;
  }
  .L127{
    background-image: url("../assets/Alphabet/127.jpg");
    background-repeat: no-repeat;
  }
  .L128{
    background-image: url("../assets/Alphabet/128.jpg");
    background-repeat: no-repeat;
  }
  .L129{
    background-image: url("../assets/Alphabet/129.jpg");
    background-repeat: no-repeat;
  }
  .L130{
    background-image: url("../assets/Alphabet/130.jpg");
    background-repeat: no-repeat;
  }
  .L131{
    background-image: url("../assets/Alphabet/131.jpg");
    background-repeat: no-repeat;
  }
  .L132{
    background-image: url("../assets/Alphabet/132.jpg");
    background-repeat: no-repeat;
  }
  .L133{
    background-image: url("../assets/Alphabet/133.jpg");
    background-repeat: no-repeat;
  }
  .L134{
    background-image: url("../assets/Alphabet/134.jpg");
    background-repeat: no-repeat;
  }
  .L135{
    background-image: url("../assets/Alphabet/135.jpg");
    background-repeat: no-repeat;
  }
  .L136{
    background-image: url("../assets/Alphabet/136.jpg");
    background-repeat: no-repeat;
  }
  .L137{
    background-image: url("../assets/Alphabet/137.jpg");
    background-repeat: no-repeat;
  }
  .L138{
    background-image: url("../assets/Alphabet/138.jpg");
    background-repeat: no-repeat;
  }
  .L139{
    background-image: url("../assets/Alphabet/139.jpg");
    background-repeat: no-repeat;
  }
  .L140{
    background-image: url("../assets/Alphabet/140.jpg");
    background-repeat: no-repeat;
  }
  .L141{
    background-image: url("../assets/Alphabet/141.jpg");
    background-repeat: no-repeat;
  }
  .L142{
    background-image: url("../assets/Alphabet/142.jpg");
    background-repeat: no-repeat;
  }
  .L143{
    background-image: url("../assets/Alphabet/143.jpg");
    background-repeat: no-repeat;
  }
  .L144{
    background-image: url("../assets/Alphabet/144.jpg");
    background-repeat: no-repeat;
  }
  .L145{
    background-image: url("../assets/Alphabet/145.jpg");
    background-repeat: no-repeat;
  }
  .L146{
    background-image: url("../assets/Alphabet/146.jpg");
    background-repeat: no-repeat;
  }
  .L147{
    background-image: url("../assets/Alphabet/147.jpg");
    background-repeat: no-repeat;
  }
  .L148{
    background-image: url("../assets/Alphabet/148.jpg");
    background-repeat: no-repeat;
  }
  .L149{
    background-image: url("../assets/Alphabet/149.jpg");
    background-repeat: no-repeat;
  }
  .L200{
    background-image: url("../assets/Alphabet/200.jpg");
    background-repeat: no-repeat;
  }
  .L211{
    background-image: url("../assets/Alphabet/211.jpg");
    background-repeat: no-repeat;
  }
  .L212{
    background-image: url("../assets/Alphabet/212.jpg");
    background-repeat: no-repeat;
  }
  .L213{
    background-image: url("../assets/Alphabet/213.jpg");
    background-repeat: no-repeat;
  }
  .L214{
    background-image: url("../assets/Alphabet/214.jpg");
    background-repeat: no-repeat;
  }
  .L215{
    background-image: url("../assets/Alphabet/215.jpg");
    background-repeat: no-repeat;
  }
  .L216{
    background-image: url("../assets/Alphabet/216.jpg");
    background-repeat: no-repeat;
  }
  .L217{
    background-image: url("../assets/Alphabet/217.jpg");
    background-repeat: no-repeat;
  }
  .L218{
    background-image: url("../assets/Alphabet/218.jpg");
    background-repeat: no-repeat;
  }
  .L219{
    background-image: url("../assets/Alphabet/219.jpg");
    background-repeat: no-repeat;
  }
  .L220{
    background-image: url("../assets/Alphabet/220.jpg");
    background-repeat: no-repeat;
  }
  .L221{
    background-image: url("../assets/Alphabet/221.jpg");
    background-repeat: no-repeat;
  }
  .L222{
    background-image: url("../assets/Alphabet/222.jpg");
    background-repeat: no-repeat;
  }
  .L223{
    background-image: url("../assets/Alphabet/223.jpg");
    background-repeat: no-repeat;
  }
  .L224{
    background-image: url("../assets/Alphabet/224.jpg");
    background-repeat: no-repeat;
  }
  .L225{
    background-image: url("../assets/Alphabet/225.jpg");
    background-repeat: no-repeat;
  }
  .L226{
    background-image: url("../assets/Alphabet/226.jpg");
    background-repeat: no-repeat;
  }
  .L227{
    background-image: url("../assets/Alphabet/227.jpg");
    background-repeat: no-repeat;
  }
  .L228{
    background-image: url("../assets/Alphabet/228.jpg");
    background-repeat: no-repeat;
  }
  .L229{
    background-image: url("../assets/Alphabet/229.jpg");
    background-repeat: no-repeat;
  }
  .L230{
    background-image: url("../assets/Alphabet/230.jpg");
    background-repeat: no-repeat;
  }
  .L231{
    background-image: url("../assets/Alphabet/231.jpg");
    background-repeat: no-repeat;
  }
  .L232{
    background-image: url("../assets/Alphabet/232.jpg");
    background-repeat: no-repeat;
  }
  .L233{
    background-image: url("../assets/Alphabet/233.jpg");
    background-repeat: no-repeat;
  }
  .L234{
    background-image: url("../assets/Alphabet/234.jpg");
    background-repeat: no-repeat;
  }
  .L235{
    background-image: url("../assets/Alphabet/235.jpg");
    background-repeat: no-repeat;
  }
  .L236{
    background-image: url("../assets/Alphabet/236.jpg");
    background-repeat: no-repeat;
  }
  .L237{
    background-image: url("../assets/Alphabet/237.jpg");
    background-repeat: no-repeat;
  }
  .L238{
    background-image: url("../assets/Alphabet/238.jpg");
    background-repeat: no-repeat;
  }
  .L239{
    background-image: url("../assets/Alphabet/239.jpg");
    background-repeat: no-repeat;
  }
  .L240{
    background-image: url("../assets/Alphabet/240.jpg");
    background-repeat: no-repeat;
  }
  .L241{
    background-image: url("../assets/Alphabet/241.jpg");
    background-repeat: no-repeat;
  }
  .L242{
    background-image: url("../assets/Alphabet/242.jpg");
    background-repeat: no-repeat;
  }
  .L243{
    background-image: url("../assets/Alphabet/243.jpg");
    background-repeat: no-repeat;
  }
  .L244{
    background-image: url("../assets/Alphabet/244.jpg");
    background-repeat: no-repeat;
  }
  .L245{
    background-image: url("../assets/Alphabet/245.jpg");
    background-repeat: no-repeat;
  }
  .L246{
    background-image: url("../assets/Alphabet/246.jpg");
    background-repeat: no-repeat;
  }
  .L247{
    background-image: url("../assets/Alphabet/247.jpg");
    background-repeat: no-repeat;
  }
  .L248{
    background-image: url("../assets/Alphabet/248.jpg");
    background-repeat: no-repeat;
  }
  .L249{
    background-image: url("../assets/Alphabet/249.jpg");
    background-repeat: no-repeat;
  }
</style>

<!-- Vue component for headers on website -->

<template>
    <div class="header" :class="{ cardHeader: cardHeader, navHeader: navHeader}"> <!-- dynamically assigning classes -->
      <slot v-if="navHeader" />
      <h1 v-else> {{ title }} </h1>
    </div>
</template>

<script>

  export default {
    name: 'HeaderComponent',
    props: {
      title: String,
      cardHeader: Boolean,
      navHeader: Boolean
    }
  }

</script>

<style scoped>
  .header {
    background-color: var(--primary);
    border: 2px solid var(--black);
    border-radius: 7px;
    text-align: center;
    padding: 10px 0;
    width: 100%;
    box-sizing: border-box;
  }

  h1 {
    font-size: 1.6rem;
  }

  .cardHeader {
    box-shadow: 0px 5px 5px var(--darkGreen);
    margin-bottom: 10px;
  }

  .navHeader {
    padding: 10px;
    margin-bottom: 16px;
  }
</style>
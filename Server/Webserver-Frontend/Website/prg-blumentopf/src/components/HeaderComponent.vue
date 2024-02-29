<!-- Vue component for headers on website -->

<template>
    <div class="header" :class="{ 'card-header': cardHeader, 'nav-header': navHeader}"> <!-- dynamically assigning classes -->
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

  h1 {
    font-size: 1.6rem;
  }

  .header {
    width: 100%;
    padding: 10px 0;
    background-color: var(--lightGreen);
    border: 2px solid var(--black);
    border-radius: 3px;
    box-sizing: border-box;
    box-shadow: 0px 5px 5px var(--darkGrey);
    text-align: center;
  }

  .card-header {
    margin-bottom: 10px;
  }

  .card-header h1 {
    margin: 0.5em 0;
  }

  .nav-header {
    padding: 10px;
    margin-bottom: 16px;
  }

  @media only screen and (min-width: 768px) {
    .card-header h1 {
      font-size: 1.4rem;
    }

    .nav-header {
      padding: 16px;
      margin-bottom: 28px;
    }
  }

  @media only screen and (min-width: 992px) {
    .card-header h1 {
      font-size: 1.6rem;
    }
  }

</style>
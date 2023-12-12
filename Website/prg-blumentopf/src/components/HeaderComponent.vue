<template>
    <div class="header" :class="{ cardHeader: type === 'cardHeader'}">
        <span> {{ title }} </span>
        <span v-if="type === 'pageHeader'" class="icon" @click="openSettings">X</span>
    </div>
</template>

<script>

  export default {
    name: 'HeaderComponent',
    props: {
      title: String,
      type: String
    },
    methods: {
      openSettings() {
        this.$emit('openSettings')
      }
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

  .cardHeader {
    box-shadow: 0px 5px 5px var(--primaryAlt);
    margin-bottom: 10px;
  }

  .icon {
    background-color: var(--secondaryAlt);
    margin-left: 10px;
  }
</style>
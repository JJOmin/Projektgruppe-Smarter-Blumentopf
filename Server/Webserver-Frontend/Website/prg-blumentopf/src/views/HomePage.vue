<template>

  <div class="indicators">
    <CardComponent v-for="(sensor, index) in sensorData" :key="sensor.name" class="indicator-card">
      <HeaderComponent :title="sensor.name" cardHeader=True />
      <IndicatorComponent :data="sensor" :boundaries="profileData.boundaries[index]" :url="urls[index]" />
    </CardComponent>
  </div>

</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'
import IndicatorComponent from '../components/IndicatorComponent.vue'

export default {
  name: 'HomePage',
  components: {
    CardComponent,
    HeaderComponent,
    IndicatorComponent
  },
  props: ['sensorData', 'profileData'],
  data() {
    return {
      urls: {
        temperature: "https://cloudleo.duckdns.org/Blumentopf/Assets/Temp-Icon.png",
        light: "https://cloudleo.duckdns.org/Blumentopf/Assets/Light-Icon.png",
        moisture: "https://cloudleo.duckdns.org/Blumentopf/Assets/Soil-Icon.png"
      }
    }
  }
}
</script>

<style scoped>
.indicators {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

.indicator-card {
  margin: 16px;
  max-width: 400px;
}

@media only screen and (min-width: 576px) {
  .indicators {
    flex-direction: row;
  }
}

</style>
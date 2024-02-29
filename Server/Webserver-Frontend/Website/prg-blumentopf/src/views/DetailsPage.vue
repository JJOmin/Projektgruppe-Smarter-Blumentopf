<!-- Vue component for details page -->

<template>

    <div class="graphs">
        <!-- create a Card with graph for every sensor -->
        <CardComponent v-for="sensor in sensorData" :key="sensor.name" class="graph-card">
            <HeaderComponent :title="sensor.name + ' (' + sensor.unit + ')'" cardHeader=True />
            <GraphComponent :log="sensor.log" :timeStamps="timeStamps" />
        </CardComponent>
    </div>

</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'
import GraphComponent from '../components/GraphComponent.vue'

export default {
    name: 'DetailsPage',
    components: {
        CardComponent,
        HeaderComponent,
        GraphComponent
    },
    props: ['sensorData', 'timeStamps']
}

</script>

<style scoped>

.graphs {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

@media only screen and (min-width: 576px) {
  .graph-card {
    width: 90%;
  }
}

@media only screen and (min-width: 768px) {
  .graph-card {
    width: 80%;
    max-width: 750px;
  }
}

@media only screen and (min-width: 1200px) {
  .graphs {
    flex-direction: row;
  }

  .graph-card {
    width: 30%;
    max-width: none;
  }
}

</style>
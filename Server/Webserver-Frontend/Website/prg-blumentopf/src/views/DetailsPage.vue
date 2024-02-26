<template>

    <div class="graphs">
        <CardComponent v-for="sensor in sensorData" :key="sensor.name" class="graph-card">
            <HeaderComponent :title="sensor.name" cardHeader=True />
            <GraphComponent :log="sensor.log" />
        </CardComponent>
        <CardComponent class="graph-card">
            <HeaderComponent title="Pumpe" cardHeader=True />
            <GraphComponent :log="[30, 0, 0, 0, 80, 0, 0, 0, 65, 0]" />
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
    props: ['sensorData']
}
</script>

<style scoped>

.graphs {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

.graph-card {
  margin: 10px;
  width: 75%;
}

@media only screen and (min-width: 576px) {
  .graphs {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .graph-card {
    width: 40%;
  }
}

</style>
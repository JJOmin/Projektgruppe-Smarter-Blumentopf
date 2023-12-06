<template>
  <div v-if="showSettings">
    <SettingsComponent @closeSettings="toggleSettings" @updatePlant="updatePlant" :plant="selectedPlant"></SettingsComponent>
  </div>

  <div v-else-if="potData && profile">
    <HeaderComponent @openSettings="toggleSettings" :title="profile ? profile.name : ''" type="pageHeader" />

    <CardComponent>
      <HeaderComponent title="Aktuelle Werte:" type="cardHeader" />
      <ul>
        <li v-for="(sensor, index) in potData.sensors" :key="index">
          <SliderComponent :title="sensor.name" :value="sensor.log[sensor.log.length - 1]" :unit="sensor.unit" :boundaries="profile.boundaries[index]"></SliderComponent>
        </li>
      </ul>
    </CardComponent>

    <CardComponent>
      <HeaderComponent title="Statistik:" type="cardHeader" />
      <TabulatorComponent :sensors="potData.sensors"></TabulatorComponent>
    </CardComponent>
  </div>
</template>

<script>

import HeaderComponent from './components/HeaderComponent.vue'
import CardComponent from './components/CardComponent.vue'
import SliderComponent from './components/SliderComponent.vue'
import TabulatorComponent from './components/TabulatorComponent.vue'
import SettingsComponent from './components/SettingsComponent.vue'

export default {
  name: 'App',
  components: {
    HeaderComponent,
    CardComponent,
    SliderComponent,
    TabulatorComponent,
    SettingsComponent
},
  data() {
    return {
      showSettings: false,
      profile: null,
      potData: null,
      selectedPlant: 'basil',
      dbUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/db.json",
      potUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/prototyp.json"
    }
  },
  methods: {
    toggleSettings() {
      this.showSettings = !this.showSettings
    },
    updatePlant(newPlant) {
      this.selectedPlant = newPlant
      this.setProfile()
    },
    setProfile() {
      fetch(this.dbUrl)
        .then(res => res.json())
        .then(data => this.profile = data[this.selectedPlant])
        .catch(err => console.log(err.message))
    }
  },
  mounted() {
    fetch(this.potUrl)
      .then(res => res.json())
      .then(data => this.potData = data)
      .catch(err => console.log(err.message))
    this.setProfile()
  }
}
</script>

<style>
#app {
  --lightGrey: #cccccc;
  --defaultGrey: #888888;
  --darkGrey: #444444;
  --black: #000000;
  --white: #ffffff;
  --primary: #7da0d1;
  --secondary: #d1ae7d;
  --statGood: #50d025;
  --statOkay: #f0ed11;
  --statAlert: #f57913;
  --statWarning: #d82816;

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--black);
}

ul {
  margin: 0;
  padding: 0;
}

li {
  list-style-type: none;
}
</style>

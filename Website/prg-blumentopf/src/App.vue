<template>
  <div v-if="showSettings">
    <SettingsComponent @closeSettings="toggleSettings" @updatePlant="updatePlant" @updateName="updateName"
    :plant="selectedPlant" :potName="this.potData.name" :profiles="profiles"></SettingsComponent>
  </div>

  <div v-else-if="potData && activeProfile">
    <HeaderComponent @openSettings="toggleSettings" :title="activeProfile ? activeProfile.name : ''" type="pageHeader" />

    <CardComponent>
      <HeaderComponent title="Aktuelle Werte:" type="cardHeader" />
      <ul>
        <li v-for="(sensor, index) in potData.sensors" :key="index">
          <SliderComponent :title="sensor.name" :value="sensor.log[sensor.log.length - 1]" :unit="sensor.unit" :boundaries="activeProfile.boundaries[index]"></SliderComponent>
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
      profiles: null,
      potData: null,
      selectedPlant: null,
      activeProfile: null,
      dbUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/db.json",
      potUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/prototyp.json",
      apiUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/api.php",
    }
  },
  methods: {
    toggleSettings() {
      this.showSettings = !this.showSettings
    },
    updatePlant(newPlant) {
      this.selectedPlant = newPlant
      this.setActiveProfile()
      this.potData.profile = this.selectedPlant
      this.writeToJson(this.potData)
    },
    updateName(newName) {
      this.potData.name = newName
      this.writeToJson(this.potData)
    },
    writeToJson(data) {

      console.log("Updating Json...")
      data = JSON.stringify(data)

      fetch(this.apiUrl, {
        method: "POST",
        body: data
      })
      .then(res => res.json())
      .then(data => console.log(data.message))
      .catch(err => console.log(err.message))

    },
    setProfiles() {
      fetch(this.dbUrl)
        .then(res => res.json())
        .then(data => {
          this.profiles = data
          this.setActiveProfile()
        })
        .catch(err => console.log(err.message))
    },
    setActiveProfile() {
      this.activeProfile = this.profiles[this.selectedPlant]
    }
  },
  mounted() {
    fetch(this.potUrl)
      .then(res => res.json())
      .then(data => {
        this.potData = data
        this.selectedPlant = this.potData.profile
        this.setProfiles()
      })
      .catch(err => console.log(err.message))
  }
}
</script>

<style>
#app {
  --white: #ffffff;
  --lightGrey: #cccccc;
  --defaultGrey: #888888;
  --darkGrey: #444444;
  --black: #000000;
  --primary: var(--pal10);
  --primaryAlt: var(--pal8);
  --secondary: var(--pal1);
  --secondaryAlt: var(--pal3);
  --statGood: #50d025;
  --statOkay: #f0ed11;
  --statAlert: #f57913;
  --statWarning: #d82816;

  --pal1: #582F0E;
  --pal2: #7F4F24;
  --pal3: #936639;
  --pal4: #A68A64;
  --pal5: #B6AD90;
  --pal6: #C2C5AA;
  --pal7: #A4AC86;
  --pal8: #656D4A;
  --pal9: #414833;
  --pal10: #333D29;

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--pal6);
}

ul {
  margin: 0;
  padding: 0;
}

li {
  list-style-type: none;
}
</style>

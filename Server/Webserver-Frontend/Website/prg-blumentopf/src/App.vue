<!-- Vue master component -->

<template>

  <!-- Navbar -->
  <HeaderComponent v-if="potData && activeProfile" navHeader=True>
    <div class="nav">
      <div class="nav-title">
        <h1>{{ potData.name }}: <span>{{ activeProfile.name }}</span></h1>
      </div>
      <!-- nav-links (getting displayed on bigger devices) -->
      <div class="nav-links">
        <router-link :to="{name: 'Home'}">Übersicht</router-link>
        <router-link :to="{name: 'Details'}">Historie</router-link>
        <router-link :to="{name: 'Profiles'}">Profile</router-link>
        <router-link :to="{name: 'Settings'}">Einstellungen</router-link>
      </div>
      <!-- hamburger icon (getting displayed on smaller devices) -->
      <div class="nav-bars" @click="toggleNavModal()">
        <div v-for="i in 3" :key="i" :class="'bar-' + i"></div>
      </div>
    </div>
  </HeaderComponent>

  <!-- navbar modal (gets toggled by hamburger icon on smaller devices) -->
  <div>
    <CardComponent v-if="navModal" class="nav-modal">
      <div>
        <router-link :to="{name: 'Home'}" @click="toggleNavModal()">Übersicht</router-link>
        <router-link :to="{name: 'Details'}" @click="toggleNavModal()">Historie</router-link>
        <router-link :to="{name: 'Profiles'}" @click="toggleNavModal()">Profile</router-link>
        <router-link :to="{name: 'Settings'}" @click="toggleNavModal()">Einstellungen</router-link>
      </div>
    </CardComponent>
  </div>

  <!-- Vue router tag with data bindings and event listeners -->
  <router-view v-if="potData && activeProfile"

  :sensorData="potData.sensors"
  :timeStamps="potData.timeStamps"
  :profileData="activeProfile"
  :defaultProfiles="defaultProfiles"
  :userProfiles="userProfiles"
  :potName="potData.name"
  
  @setProfile="updatePlant"
  @createProfile="createProfile"
  @deleteProfile="deleteProfile"
  @applyChanges="applyChanges"
  @deleteLogs="deleteLogs"
  @reset="reset"
  />

</template>

<script>


import CardComponent from './components/CardComponent.vue'
import HeaderComponent from './components/HeaderComponent.vue'

export default {
  name: 'App',
  components: {
    HeaderComponent,
    CardComponent
  },
  data() {
    return {
      // Server links
      dbUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/db.json",
      potUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/prototyp.json",
      apiUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/api.php",
      // Initial Variables
      potData: null, // data from prototyp.json
      defaultProfiles: null, // default profiles from db.json
      userProfiles: null, // user profiles from prototyp.json
      selectedProfile: null, // name of currently selected profile
      activeProfile: null, // data of currently selected profile
      navModal: false // boolean for visibility of nav modal
    }
  },
  methods: {
    // function for resetting prototyp.json data
    reset() {
      this.potData = {
        name: "Prototyp 1.0",
        selectedPlant: "basil",
        profiles: {
          dragonTree: {
            name: "Drachenbaum",
            boundaries: {
              temperature: {
                min: 15,
                max: 40
              },
              light: {
                min: 1000,
                max: 8000
              },
              moisture: {
                min: 10,
                max: 50
              }
            }
          }
        },
        timeStamps: [
          {"year": 2024, "month": 2, "day": 5, "hour": 13, "minute": 43},
          {"year": 2024, "month": 2, "day": 6, "hour": 7, "minute": 25},
          {"year": 2024, "month": 2, "day": 7, "hour": 14, "minute": 47},
          {"year": 2024, "month": 2, "day": 8, "hour": 12, "minute": 11},
          {"year": 2024, "month": 2, "day": 9, "hour": 18, "minute": 8},
          {"year": 2024, "month": 2, "day": 11, "hour": 15, "minute": 56},
          {"year": 2024, "month": 2, "day": 13, "hour": 20, "minute": 37},
          {"year": 2024, "month": 2, "day": 15, "hour": 6, "minute": 52},
          {"year": 2024, "month": 2, "day": 18, "hour": 21, "minute": 31},
          {"year": 2024, "month": 2, "day": 20, "hour": 17, "minute": 33}
        ],
        sensors: {
          temperature: {
            name: "Temperatur",
            unit: "°C",
            status: "Warning",
            log: [31, 20, 12, 20, 19, 34, 27, 34, 10, 14]
          },
          light: {
            name: "Licht",
            unit: "lx",
            status: "Okay",
            log: [810, 1849, 1813, 1069, 440, 1377, 787, 488, 531, 1581]
          },
          moisture: {
            name: "Bodenfeuchtigkeit",
            unit: "%",
            status: "Okay",
            log: [44, 50, 53, 55, 49, 84, 74, 61, 54, 74]
          }
        }
      }
      this.writeToJson(this.potData)
    },
    // function for changing the name of the pot
    applyChanges(newName) {
      this.potData.name = newName
      this.writeToJson(this.potData)
    },
    // function for deleting all logs
    deleteLogs() {
      if (confirm("Möchtest du wirklich alle gemessenen Werte zurücksetzen?")) {
        this.potData.timeStamps = []
        for (let sensor in this.potData.sensors) {
          this.potData.sensors[sensor].log = []
          this.potData.sensors[sensor].status = ""
        }
        this.writeToJson(this.potData)
      }
    },
    // function for selecting a profile
    updatePlant(newPlant) {
      this.selectedProfile = newPlant
      this.setActiveProfile()
      this.potData.selectedPlant = this.selectedProfile
      this.checkBoundaries()
      this.writeToJson(this.potData)
    },
    // function for creating a new profile
    createProfile(profile) {
      let key = this.checkKey(profile.name)
      if (key != false) {
        this.potData.profiles[key] = profile
        console.log(this.potData.profiles)
        this.userProfiles = this.potData.profiles
        this.writeToJson(this.potData)
        setTimeout(this.$router.go, 1000)
      }
    },
    // function for deleting a profile
    deleteProfile(profile) {
      if (confirm("Soll das folgende Profil wirklich gelöscht werden?\n" + this.potData.profiles[profile].name)){
        if (this.selectedProfile != profile) {
          delete this.potData.profiles[profile]
          this.userProfiles = this.potData.profiles
          this.writeToJson(this.potData)
          setTimeout(this.$router.go, 1000)
        } else {
          alert("Das aktive Profil kann nicht gelöscht werden!")
        }
      }
    },
    // function for validation of key (or index) of a new profile
    checkKey(key) {
      if (/[^A-Za-z\s]/g.test(key)) {
        alert("Der Name darf keine Zahlen oder Sonderzeichen enthalten!")
        return false
      } else {

        let lowerKey = key.toLowerCase()
        let newKey = lowerKey.replace(/[\s](.)/g, function($1, $2) {return $2.toUpperCase()})

        for (let profile in this.defaultProfiles) {
          if (this.defaultProfiles[profile].name === key || profile === newKey) {
            alert("Profilname schon in Default Profiles vorhanden!")
            return false
          }
        }

        for (let profile in this.userProfiles) {
          if (this.userProfiles[profile].name === key || profile === newKey) {
            alert("Profilname schon in User Profiles vorhanden!")
            return false
          }
        }

        return newKey
      }
    },
    // function for writing data to server
    writeToJson(data) {

      console.log(data)
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
    // function for reading prototyp.json from server
    readFromJson() {
      fetch(this.potUrl)
        .then(res => res.json())
        .then(data => {
          this.potData = data
          this.selectedProfile = this.potData.selectedPlant
          this.setProfiles()
        })
        .catch(err => console.log(err.message))
    },
    // function for reading db.json from server
    setProfiles() {
      fetch(this.dbUrl)
        .then(res => res.json())
        .then(data => {
          this.defaultProfiles = data.profiles
          this.userProfiles = this.potData.profiles
          this.setActiveProfile()
          this.checkBoundaries()
        })
        .catch(err => console.log(err.message))
    },
    // function for setting the active profile data
    setActiveProfile() {
      
      for (let profile in this.defaultProfiles) {
        if (profile === this.selectedProfile) {
          this.activeProfile = this.defaultProfiles[profile]
        }
      }

      for (let profile in this.userProfiles) {
        if (profile === this.selectedProfile) {
          this.activeProfile = this.userProfiles[profile]
        }
      }

    },
    // function for comparing the current values with the boundaries and updating the status of the sensors
    checkBoundaries() {
      let boundaries = this.activeProfile.boundaries
      let sensors = this.potData.sensors

      for (let sensor in sensors) {
        let log = sensors[sensor].log
        if (log.length === 0) {
          break
        }
        let value = log[log.length - 1]
        if (value >= boundaries[sensor].min && value <= boundaries[sensor].max) {
          this.potData.sensors[sensor].status = "Okay"
        } else {
          this.potData.sensors[sensor].status = "Warning"
        }
      }

    },
    // function for toggling the nav modal
    toggleNavModal() {
      this.navModal = !this.navModal
    }
  },
  mounted() {
    this.readFromJson() // gets executed upon loading the page
  },
  created() {
    // updating the data from prototyp.json every 60 seconds
    let updateServerData = true
    if(updateServerData) {
      setInterval(() => {
        this.readFromJson()
      }, 60000)
    }
  }
}
</script>

<style>

html {
  height: 100%;
  margin: 0;
}

body {
  --white: #ffffff;
  --lightGrey: #cccccc;
  --defaultGrey: #888888;
  --darkGrey: #444444;
  --black: #000000;
  
  --statGood: #9CC95C;
  --statWarning: #ff6961;

  --lightGreen: #c7d6c1;
  --darkGreen: #415b39;

  padding: 1rem;
  margin: 0;
  background: linear-gradient(0deg, var(--defaultGrey) 2%, transparent 2%) 50px, linear-gradient(90deg, var(--defaultGrey) 2%, transparent 2%) 50px;
  background-size: 100px 100px;
}

#app {
  color: var(--black);
  font-family: "Comic Sans MS", "Comic Sans", serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 1.125rem;
}

ul {
  padding: 0;
  margin: 0 20px;
}

li {
  list-style-type: none;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav h1 {
  font-size: 1.6rem;
}

.nav-title {
  margin: 0 1rem;
}

.nav-title span {
  color: var(--darkGreen);
  font-style: italic;
}

.nav-links {
  display: none;
}

.nav-bars div {
  width: 30px;
  height: 4px;
  margin: 5px 0;
  background-color: var(--black);
  border-radius: 2px;
}

.nav-modal {
  margin: 0;
}

.nav-modal div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  padding-top: 10px;
}

.nav a,
.nav-modal a {
  padding: 0.4em 0.6em;
  margin-left: 0.4rem;
  border-radius: 3px;
  color: var(--black);
  text-decoration: none;
  font-size: 1.125rem;
  font-weight: bold;
}

.nav a.router-link-exact-active,
.nav-modal a.router-link-exact-active {
  background-color: var(--darkGreen);
  color: var(--white);
}

@media only screen and (min-width: 768px) {
  #app {
    font-size: 1rem;
  }

  .nav-links {
    display: inline-block;
  }

  .nav-bars,
  .nav-modal {
    display: none;
  }
}

@media only screen and (min-width: 992px) {
  #app {
    font-size: 1.125rem;
  }
}

</style>

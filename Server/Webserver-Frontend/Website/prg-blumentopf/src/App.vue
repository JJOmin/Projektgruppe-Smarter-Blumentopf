<template>
  <HeaderComponent v-if="potData && activeProfile" navHeader=True>
    <div id="nav">
      <div id="nav-logo">
        <h1>LOGO</h1>
      </div>
      <div id="nav-title">
        <h1>{{ potData.name }}: {{ activeProfile.name }}</h1>
      </div>
      <div id="nav-links">
        <router-link :to="{name: 'Home'}">Home</router-link>
        <router-link :to="{name: 'Details'}">Details</router-link>
        <router-link :to="{name: 'Profiles'}">Profiles</router-link>
        <router-link :to="{name: 'Settings'}">Settings</router-link>
      </div>
      <div id="nav-bars" @click="toggleNavModal()">
        <div v-for="i in 3" :key="i" :class="'bar-' + i"></div>
      </div>
    </div>
  </HeaderComponent>

  <CardComponent v-if="navModal" id="nav-modal">
    <div>
      <router-link :to="{name: 'Home'}">Home</router-link>
      <router-link :to="{name: 'Details'}">Details</router-link>
      <router-link :to="{name: 'Profiles'}">Profiles</router-link>
      <router-link :to="{name: 'Settings'}">Settings</router-link>
    </div>
  </CardComponent>

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
      dbUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/db.json",
      potUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/prototyp.json",
      apiUrl: "https://cloudleo.duckdns.org/Blumentopf/Database/api.php",
      potData: null,
      defaultProfiles: null,
      userProfiles: null,
      selectedProfile: null,
      activeProfile: null,
      navModal: false
    }
  },
  methods: {
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
    applyChanges(newName) {
      this.potData.name = newName
      this.writeToJson(this.potData)
    },
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
    updatePlant(newPlant) {
      this.selectedProfile = newPlant
      this.setActiveProfile()
      this.potData.selectedPlant = this.selectedProfile
      this.checkBoundaries()
      this.writeToJson(this.potData)
    },
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
    setProfiles() {
      fetch(this.dbUrl)
        .then(res => res.json())
        .then(data => {
          this.defaultProfiles = data.profiles
          this.userProfiles = this.potData.profiles
          this.setActiveProfile()
        })
        .catch(err => console.log(err.message))
    },
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
    toggleNavModal() {
      this.navModal = !this.navModal
    }
  },
  mounted() {
    this.readFromJson()
  },
  created() {
    let updateServerData = false
    if(updateServerData) {
      setInterval(() => {
        this.readFromJson()
      }, 60000)
    }
  }
}
</script>

<style>

body {
  --white: #ffffff;
  --lightGrey: #cccccc;
  --defaultGrey: #888888;
  --darkGrey: #444444;
  --black: #000000;
  --primary: var(--lightGreen);
  --primaryAlt: var(--darkGreen);
  --secondary: var(--pal11);
  --secondaryAlt: var(--darkBrown);
  --statGood: var(--pastelGreen);
  --statWarning: var(--pastelRed);
  /*
  --statGood: #50d025;
  --statOkay: #f0ed11;
  --statAlert: #f57913;
  --statWarning: #d93535;
  */

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

  --pal11: #8F7289;
  --pal12: #926972;
  --pal13: #52384D;
  --pal14: #4F6343;


  --lightGreen: #98c786;
  --altGreen: #7fa86f;
  --darkGreen: #415b39;
  --lightBrown: #e0b579;
  --darkBrown: #6e4e29;

  --beige: #ebd5a2;
  --pastelGreen: #9CC95C;
  --pastelRed: #ff6961;

  background-color: var(--white);
  margin: 0;
  padding: 10px;
}

#app {

  /*font-family: Avenir, Helvetica, Arial, sans-serif;*/
  font-family: "Comic Sans MS", "Comic Sans", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 1.125rem;
  color: var(--black);
}

ul {
  margin: 0 20px;
  padding: 0;
}

li {
  list-style-type: none;
}

#nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#nav-modal div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  padding-top: 10px;
}

#nav h1 {
  margin: 0;
  font-size: 1.6rem;
}

#nav a,
#nav-modal a {
  font-weight: bold;
  color: var(--black);
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

#nav a.router-link-exact-active,
#nav-modal a.router-link-exact-active {
  color: var(--white);
  background-color: var(--darkGreen);
}

#nav-links,
#nav-logo {
  display: none;
}

#nav-title {
  margin: 0 10px;
}

#nav-bars div {
  width: 30px;
  height: 4px;
  background-color: black;
  margin: 5px 0;
  border-radius: 2px;
}

@media only screen and (min-width: 576px) {
  #nav-links,
  #nav-logo {
    display: inline-block;
  }

  #nav-bars,
  #nav-modal {
    display: none;
  }
}

</style>

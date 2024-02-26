<template>
  <HeaderComponent v-if="potData && activeProfile" navHeader=True>
    <div id="nav">
      <div>
        <h1>LOGO</h1>
      </div>
      <div>
        <h1>{{ potData.name }} // {{ activeProfile.name }}</h1>
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
  :profileData="activeProfile"
  :defaultProfiles="defaultProfiles"
  :userProfiles="userProfiles"
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
    /*updatePlant(newPlant) {
      this.selectedPlant = newPlant
      this.setActiveProfile()
      this.potData.profile = this.selectedPlant
      this.writeToJson(this.potData)
    },
    updateName(newName) {
      this.potData.name = newName
      this.writeToJson(this.potData)
    },*/
    /*writeToJson(data) {

      console.log("Updating Json...")
      data = JSON.stringify(data)

      fetch(this.apiUrl, {
        method: "POST",
        body: data
      })
      .then(res => res.json())
      .then(data => console.log(data.message))
      .catch(err => console.log(err.message))

    },*/
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
    toggleNavModal() {
      this.navModal = !this.navModal
    }
  },
  mounted() {
    this.readFromJson()
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
  --secondary: var(--lightBrown);
  --secondaryAlt: var(--darkBrown);
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

  --lightGreen: #70ae58;
  --darkGreen: #215112;
  --lightBrown: #926631;
  --darkBrown: #392814;

  background-color: var(--darkGreen);
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
}

#nav h1 {
  margin: 0;
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

#nav-links {
  display: none;
}

#nav-bars div {
  width: 30px;
  height: 4px;
  background-color: black;
  margin: 5px 0;
  border-radius: 2px;
}

@media only screen and (min-width: 576px) {
  #nav-links {
    display: inline-block;
  }

  #nav-bars,
  #nav-modal {
    display: none;
  }
}

</style>

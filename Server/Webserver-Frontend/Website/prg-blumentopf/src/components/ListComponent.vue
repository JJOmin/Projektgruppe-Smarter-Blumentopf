<!-- Vue component for profile lists on profiles page -->

<template>

    <div class="profiles-wrapper">
        <div class="profiles">
            <h2>{{ title }}</h2>
            <!-- creating a div container for every profile -->
            <div v-for="(profile, index) in profiles" :key="index">
                <hr class="separator">
                <!-- profile header -->
                <h3>{{ profile.name }}</h3>
                <div class="profile-header" :class="{'std-header': title === 'Standard' && isVisible != index}">
                    <span class="btn" @click="toggleList(index)">Info</span>
                    <span class="btn cta-btn" @click="setProfile(index)">Aktivieren</span>
                </div>
                <!-- list with detailled infos for boundaries -->
                <ul :class="[index === isVisible ? 'visible' : 'hidden']">
                    <li class="li-header">Temperatur:</li>
                    <li class="li-tab">{{ profile.boundaries.temperature.min }} - {{ profile.boundaries.temperature.max }}</li>
                    <li class="li-header">Licht:</li>
                    <li class="li-tab">{{ profile.boundaries.light.min }} - {{ profile.boundaries.light.max }}</li>
                    <li class="li-header">Bodenfeuchtigkeit:</li>
                    <li class="li-tab">{{ profile.boundaries.moisture.min }} - {{ profile.boundaries.moisture.max }}</li>
                    <li :class="{'li-btn': title === 'Nutzer'}"><span v-if="title === 'Nutzer'" class="btn" @click="deleteProfile(index)">Profil löschen</span></li>
                </ul>
            </div>
            <!-- div container for creating a new profile -->
            <div v-if="title === 'Nutzer'">
                <hr class="separator">
                <div class="new-profile">
                    <h3 class="btn" @click="toggleList(true)">Neues Profil anlegen</h3>
                </div>
                <!-- list for user inputs -->
                <ul :class="[true === isVisible ? 'visible' : 'hidden']">
                    <li class="li-header">Name:</li>
                    <li class="li-tab"><input class="txt" type="text" v-model="newProfile.name"></li>
                    <li class="li-header">Temperatur:</li>
                    <li class="li-tab">Min: <input class="num" type="number" v-model="newProfile.boundaries.temperature.min"></li>
                    <li class="li-tab">Max: <input class="num" type="number" v-model="newProfile.boundaries.temperature.max"></li>
                    <li class="li-header">Licht:</li>
                    <li class="li-tab">Min: <input class="num" type="number" v-model="newProfile.boundaries.light.min"></li>
                    <li class="li-tab">Max: <input class="num" type="number" v-model="newProfile.boundaries.light.max"></li>
                    <li class="li-header">Bodenfeuchtigkeit:</li>
                    <li class="li-tab">Min: <input class="num" type="number" v-model="newProfile.boundaries.moisture.min"></li>
                    <li class="li-tab">Max: <input class="num" type="number" v-model="newProfile.boundaries.moisture.max"></li>
                    <li class="li-btn"><span class="btn" @click="createProfile">Profil erstellen</span></li>
                </ul>
            </div>
        </div>
    </div>

</template>

<script>

  export default {
    name: 'ListComponent',
    props: {
      title: String,
      profiles: Object
    },
    methods: {
        // event for selecting a profile
        setProfile(profile) {
            this.$emit('setProfile', profile)
        },
        // event for deleting a profile
        deleteProfile(profile) {
            this.$emit('deleteProfile', profile)
        },
        // event for creating a new profile
        createProfile() {
            this.$emit('createProfile', this.newProfile)
        },
        // function for toggling visibility of profile details
        toggleList(listName) {
            console.log(listName)
            if (this.isVisible != listName) {
                this.isVisible = listName
            } else {
                this.isVisible = null
            }
        }
    },
    data() {
        return {
            isVisible: null,
            // standard values for new profiles
            newProfile: {
                name: "Neues Profil",
                boundaries: {
                    temperature: {
                        min: 0,
                        max: 100
                    },
                    light: {
                        min: 0,
                        max: 10000
                    },
                    moisture: {
                        min: 0,
                        max: 100
                    }
                }
            }
        }
    }
  }

</script>

<style scoped>

h2 {
    margin-top: 0.4em;
    margin-bottom: 0.7em;
    font-size: 1.4rem;
}

h3 {
    display: block;
    width: 100%;
    color: var(--darkGreen);
    text-align: center;
    font-size: 1.2rem;
    font-style: italic;
}

h3.btn {
    width: 80%;
}

.profiles-wrapper {
    display: flex;
    justify-content: space-around;
}

.profiles {
    width: 90%;
    max-width: 400px;
    padding: 10px;
}

.profiles div:first-of-type hr {
    display: none;
}

.profiles div:last-of-type .std-header {
    margin-bottom: 0;
}

.profile-header {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-bottom: 1.2rem;
}

.new-profile {
    display: flex;
    justify-content: space-around;
}

.new-profile h3 {
    margin-top: 0;
}

.separator {
    margin: 1.5rem;
    border: 1px solid var(--defaultGrey);
    border-radius: 1px;
}

ul {
    margin-left: 20%;
}

.li-header {
    margin: 0.4rem 0;
}

.li-tab {
    margin-left: 2.4rem;
    list-style-type: square;
}

.li-btn {
    margin: 1.4rem 0;
    font-size: 0.8rem;
}

.btn {
    padding: 0.4em 0.6em;
    background-color: var(--white);
    border: 1px solid var(--darkGrey);
    border-radius: 3px;
    box-shadow: 0px 2px 2px var(--darkGrey);
    color: var(--darkGreen);
    font-weight: bold;
}

.cta-btn {
    background-color: var(--darkGreen);
    color: var(--white);
}

.visible {
    display: block;
}

.hidden {
    display: none;
}

input {
    margin-top: 10px;
    background-color: var(--white);
    border: 1px solid var(--darkGrey);
    border-radius: 2px;
}

.num {
    width: 50px;
}

.txt {
    width: 120px;
}

@media only screen and (min-width: 576px) {
    .profiles {
        width: 80%;
        max-width: 500px;
    }
}

</style>
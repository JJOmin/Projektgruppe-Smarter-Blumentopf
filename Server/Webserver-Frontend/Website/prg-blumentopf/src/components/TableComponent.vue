<!-- Vue component for profile tables on profiles page -->

<template>

    <div>
        <table>
            <tr>
                <th>{{ title }}</th>
            </tr>
            <!-- Header row -->
            <tr>
                <th rowspan="2">Name</th>
                <th colspan="2">Temperatur (°C)</th>
                <th colspan="2">Licht (lx)</th>
                <th colspan="2">Bodenfeuchtigkeit (%)</th>
                <th rowspan="2">Auswahl</th>
                <th v-if="title === 'User Profiles'" rowspan="2">Löschen</th>
            </tr>
            <tr>
                <th>min</th>
                <th>max</th>
                <th>min</th>
                <th>max</th>
                <th>min</th>
                <th>max</th>
            </tr>
            <!-- Data row -->
            <tr v-for="(profile, index) in profiles" :key="index">
                <td>{{ profile.name }}</td>
                <td>{{ profile.boundaries.temperature.min }}</td>
                <td>{{ profile.boundaries.temperature.max }}</td>
                <td>{{ profile.boundaries.light.min }}</td>
                <td>{{ profile.boundaries.light.max }}</td>
                <td>{{ profile.boundaries.moisture.min }}</td>
                <td>{{ profile.boundaries.moisture.max }}</td>
                <td><span class="btn" @click="setProfile(index)">Profil auswählen</span></td>
                <td v-if="title === 'User Profiles'"><span class="btn" @click="deleteProfile(index)">Profil löschen</span></td>
            </tr>
            <tr v-if="title === 'User Profiles'">
                <td>Name: <input type="text" v-model="newProfile.name"></td>
                <td>Temp Min: <input type="number" v-model="newProfile.boundaries.temperature.min"></td>
                <td>Temp Max: <input type="number" v-model="newProfile.boundaries.temperature.max"></td>
                <td>Light Min: <input type="number" v-model="newProfile.boundaries.light.min"></td>
                <td>Light Max: <input type="number" v-model="newProfile.boundaries.light.max"></td>
                <td>Moist Min: <input type="number" v-model="newProfile.boundaries.moisture.min"></td>
                <td>Moist Max: <input type="number" v-model="newProfile.boundaries.moisture.max"></td>
                <td><span class="btn" @click="createProfile">Profil erstellen</span></td>
            </tr>
        </table>
    </div>

</template>

<script>

  export default {
    name: 'TableComponent',
    props: {
      title: String,
      profiles: Object
    },
    methods: {
        setProfile(profile) {
            this.$emit('setProfile', profile)
        },
        deleteProfile(profile) {
            this.$emit('deleteProfile', profile)
        },
        createProfile() {
            this.$emit('createProfile', this.newProfile)
        }
    },
    data() {
        return {
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

table {
    margin: 10px;
}

.btn {
    background-color: var(--darkGreen);
    border-radius: 3px;
    padding: 5px;
    font-weight: bold;
    color: var(--white);
}

</style>
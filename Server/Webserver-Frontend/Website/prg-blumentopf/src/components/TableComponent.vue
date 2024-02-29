<!-- Vue component for profile tables on profiles page -->

<template>

    <div class="table-wrapper">
        <h2>{{ title }}</h2>
        <table>
            <!-- Header row -->
            <tr class="header">
                <th rowspan="2">Name</th>
                <th colspan="2">Temperatur (°C)</th>
                <th colspan="2">Licht (lx)</th>
                <th colspan="2">Bodenfeuchtigkeit (%)</th>
                <th rowspan="2">Aktionen</th>
            </tr>
            <!-- Sub Header row -->
            <tr class="sub-header">
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
                <td><span v-if="title === 'Nutzer'" class="btn" @click="deleteProfile(index)">Löschen</span> <!-- 'Löschen' button only gets displayed for User Profiles -->
                <span class="btn cta-btn" @click="setProfile(index)">Aktivieren</span></td>
            </tr>
            <!-- input row for creating profiles -->
            <tr v-if="title === 'Nutzer'">
                <td><input class="txt" type="text" v-model="newProfile.name"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.temperature.min"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.temperature.max"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.light.min"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.light.max"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.moisture.min"></td>
                <td><input class="num" type="number" v-model="newProfile.boundaries.moisture.max"></td>
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
        }
    },
    data() {
        return {
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
    margin: 0.2em 0;
    text-align: left;
    font-size: 1.4rem;
}

.table-wrapper {
    padding: 12px;
}

table {
    width: 100%;
    border-radius: 3px;
}

table, th, td {
    border: 1px solid var(--defaultGrey);
    border-spacing: 0;
}

th {
    padding: 10px 6px;
    background-color: var(--defaultGrey);
    white-space: nowrap;
}

td {
    padding: 10px 6px;
    background-color: var(--white);
    text-align: center;
    white-space: nowrap;
}

td:first-of-type {
    color: var(--darkGreen);
    text-align: left;
    font-style: italic;
}

td:last-of-type {
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.header th {
    width: 20%;
}

.sub-header th {
    width: 10%;
}

.btn {
    padding: 0.4em 0.4em;
    background-color: var(--white);
    border: 1px solid var(--darkGrey);
    border-radius: 3px;
    box-shadow: 0px 2px 2px var(--darkGrey);
    color: var(--darkGreen);
    font-size: 0.8rem;
    font-weight: bold;
}

.cta-btn {
    background-color: var(--darkGreen);
    color: var(--white);
}

input {
    background-color: var(--white);
    border: 1px solid var(--darkGrey);
    border-radius: 2px;
}

.num {
    width: 40px;
}

.txt {
    width: 100px;
}

</style>
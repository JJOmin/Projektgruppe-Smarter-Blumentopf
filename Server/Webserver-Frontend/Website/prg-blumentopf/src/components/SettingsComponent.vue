<template>
    <div class="settings" @click.self="closeSettings">
        <h1>SETTINGS</h1>
        <p>
            <span>Blumentopfname:</span>
            <input type="text" v-model="newName" />
            <button @click="updateName">Namen übernehmen</button>
        </p>
        <div>
            <h3>Profiles:</h3>
            <table>
                <tr>
                    <th rowspan="2">Name</th>
                    <th colspan="2">Temperatur</th>
                    <th colspan="2">Licht</th>
                    <th colspan="2">Bodenfeuchtigkeit</th>
                    <th rowspan="2">Auswahl</th>
                </tr>
                <tr>
                    <th>min</th>
                    <th>max</th>
                    <th>min</th>
                    <th>max</th>
                    <th>min</th>
                    <th>max</th>
                </tr>
                <tr v-for="(profile, index) in profiles" :key="index" :class="profile.name === plant ? 'active' : ''">
                    <td>{{ profile.name }}</td>
                    <td>{{ profile.boundaries.temperature.min }}</td>
                    <td>{{ profile.boundaries.temperature.max }}</td>
                    <td>{{ profile.boundaries.light.min }}</td>
                    <td>{{ profile.boundaries.light.max }}</td>
                    <td>{{ profile.boundaries.moisture.min }}</td>
                    <td>{{ profile.boundaries.moisture.max }}</td>
                    <td><button @click="updatePlant(index)">Profil auswählen</button></td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'SettingsComponent',
        props: {
            plant: String,
            potName: String,
            profiles: Object
        },
        data() {
            return {
                selectedPlant: this.plant ? this.plant : "",
                newName: this.potName ? this.potName : ""
            }
        },
        methods: {
            closeSettings() {
                this.$emit('closeSettings')
            },
            updatePlant(newPlant) {
                this.$emit('updatePlant', newPlant)
            },
            updateName() {
                this.$emit('updateName', this.newName)
            }
        }
    }
</script>

<style scoped>
    .settings {
        top: 0;
        position: fixed;
        background-color: var(--secondary);
        height: 100%;
        width: 100%;
    }

    .active {
        background-color: var(--primary);
    }
</style>
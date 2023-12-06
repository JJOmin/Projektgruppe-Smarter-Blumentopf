<template>
    <div class="settings" @click.self="closeSettings">
        <p>SETTINGS</p>
        <p>
            <select v-model="selectedPlant" id="selectedPlant">
                <option value="basil">Basilikum</option>
                <option value="monstera">Monstera</option>
                <option value="dragonTree">Drachenbaum</option>
            </select>
            <button @click="updatePlant">Neue Pflanze übernehmen!</button>
        </p>
    </div>
</template>

<script>
    export default {
        name: 'SettingsComponent',
        props: {
            plant: String
        },
        data() {
            return {
                selectedPlant: this.plant ? this.plant : ""
            }
        },
        methods: {
            closeSettings() {
                this.$emit('closeSettings')
            },
            updatePlant() {
                this.$emit('updatePlant', this.selectedPlant)
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
</style>
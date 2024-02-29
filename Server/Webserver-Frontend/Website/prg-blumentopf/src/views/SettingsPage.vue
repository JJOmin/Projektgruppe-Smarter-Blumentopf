<!-- Vue component for settings page -->

<template>

    <div class="settings-wrapper">
        <CardComponent class="settings-card">
            <HeaderComponent title="Einstellungen" cardHeader=True />
            <div class="settings">
                <!-- change pot name -->
                <p><span>Topfname: <br><input class="txt" type="text" v-model="newName"></span></p>
                <p><span class="btn" @click="applyChanges">Änderungen übernehmen</span></p>
                <!-- delete logs -->
                <p><span class="btn" @click="deleteLogs">Log zurücksetzen</span></p>
                <!-- reset prototype.json on server for testing and debugging -->
                <p><span class="btn" @click="reset">Testdaten</span></p>
            </div>
        </CardComponent>
    </div>
        
</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'

export default {
    name: 'SettingsPage',
    components: {
        CardComponent,
        HeaderComponent
    },
    props: ['potName'],
    data() {
        return {
            newName: this.potName
        }
    },
    methods: {
        // event for applying setting changes
        applyChanges() {
            this.$emit('applyChanges', this.newName)
        },
        // event for deleting logs
        deleteLogs(){
            this.$emit('deleteLogs')
        },
        // event for resetting prototyp.json
        reset() {
            this.$emit('reset')
        }
    }
}
</script>

<style scoped>

.settings-wrapper {
    display: flex;
    justify-content: space-around;
}

.settings-card {
    max-width: 500px;
}

.settings {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;
    padding: 10px;
    text-align: center;
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

input {
    margin-top: 10px;
    background-color: var(--white);
    border: 1px solid var(--darkGrey);
    border-radius: 2px;
}

.txt {
    width: 120px;
}

@media only screen and (min-width: 768px) {
    .settings-card {
        width: 70%;
        max-width: 750px;
    }
}

</style>
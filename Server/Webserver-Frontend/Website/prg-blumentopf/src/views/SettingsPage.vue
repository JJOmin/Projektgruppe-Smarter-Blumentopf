<template>

    <CardComponent>
        <HeaderComponent title="Settings" cardHeader=True />
        <div class="settings">
            <p><span>Topfnamen: <input type="text" v-model="newName"></span></p>
            <p><span class="btn" @click="applyChanges">Änderungen übernehmen</span></p>
            <p><span class="btn" @click="deleteLogs">Log zurücksetzen</span></p>
            <p><span class="btn" @click="reset">Prototyp.json zurücksetzen // nur zum Testen ;-) </span></p>
        </div>
        <!--
        <ul>
            <li></li>
            <li>Diagrammhintergrund</li>
            <li>intervallzeit</li>
            <li>serverintervall</li>
            <li>nachtmodus start & endzeit</li>
            <li>Log Anzahl Werte</li>
        </ul>
        -->
    </CardComponent>
        
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
        applyChanges() {
            this.$emit('applyChanges', this.newName)
        },
        deleteLogs(){
            this.$emit('deleteLogs')
        },
        reset() {
            this.$emit('reset')
        }
    }
}
</script>

<style scoped>

.settings {
    padding: 10px;
}

.btn {
    background-color: var(--darkGreen);
    border-radius: 3px;
    padding: 5px;
    font-weight: bold;
    color: var(--white);
}

</style>
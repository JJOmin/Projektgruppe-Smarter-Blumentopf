<template>

    <CardComponent>
        <HeaderComponent title="Settings" cardHeader=True />
        <ul>
            <li>Topfnamen</li>
            <li>Diagrammhintergrund</li>
            <li>intervallzeit</li>
            <li>serverintervall</li>
            <li>nachtmodus start & endzeit</li>
        </ul>
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
    }
}
</script>

<style scoped>

</style>
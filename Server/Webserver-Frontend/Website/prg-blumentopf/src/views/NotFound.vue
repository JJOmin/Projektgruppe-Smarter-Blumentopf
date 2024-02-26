<template>
    
    <CardComponent>
        <HeaderComponent title="ERROR 404" cardHeader=True />
        <ul>
            <li><h1>Page Not Found</h1></li>
            <li><h2>Page Not Found</h2></li>
            <li><h3>Page Not Found</h3></li>
            <li><h4>Page Not Found</h4></li>
            <li><h5>Page Not Found</h5></li>
            <li><h6>Page Not Found</h6></li>
        </ul>
    </CardComponent>

</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'

export default {
    name: 'NotFound',
    components: {
        CardComponent,
        HeaderComponent
    }
}
</script>

<style scoped>

</style>
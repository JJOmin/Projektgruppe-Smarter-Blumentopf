<!-- Vue component for Error 404 page -->

<template>

    <div class="error-wrapper">
        <CardComponent class="error-card">
            <HeaderComponent title="ERROR 404" cardHeader=True />
            <div class="text-wrapper">
                <h1>Sorry, this Page does not exist!</h1>
            </div>
        </CardComponent>
    </div>

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

.error-wrapper {
    display: flex;
    justify-content: space-around;
}

.text-wrapper {
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 2rem 2rem;
}

@media only screen and (min-width: 768px) {

    .error-card {
        width: 70%;
        max-width: 850px;
    }
    .text-wrapper {
        padding: 5rem 8rem;
    }

    h1 {
        font-size: 200%;
    }
}

</style>
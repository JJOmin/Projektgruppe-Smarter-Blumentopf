<!-- Vue component for cards on website -->

<template>
    <div class="card">
        <slot />
    </div>
</template>

<script>
    export default {
        name: 'CardComponent'
    }
</script>

<style scoped>
    .card {
        width: 100%;
        padding-bottom: 10px;
        margin: 1rem 0;
        background-color: var(--lightGreen);
        border-radius: 3px;
        box-shadow: 0px 5px 5px var(--darkGrey);
    }

    @media only screen and (min-width: 576px) {
        .card {
            padding-bottom: 20px;
        }
    }
</style>
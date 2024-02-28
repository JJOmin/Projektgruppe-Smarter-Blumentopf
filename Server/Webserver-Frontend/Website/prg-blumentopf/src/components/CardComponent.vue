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
        background-color: var(--altGreen);
        width: 100%;
        border-radius: 15px;
        margin: 10px 0;
        padding-bottom: 10px;
    }
</style>
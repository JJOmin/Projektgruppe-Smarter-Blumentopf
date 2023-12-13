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
        background-color: var(--secondary);
        width: 100%;
        border-radius: 15px;
        margin: 10px 0;
        padding-bottom: 10px;
    }
</style>
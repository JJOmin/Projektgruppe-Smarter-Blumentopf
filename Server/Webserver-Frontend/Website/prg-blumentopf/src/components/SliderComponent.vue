<template>
    <div class="slider">
        <span>{{ title }}: {{ value }} {{ unit }}</span>
        <span class="indicator" :class="checkBoundaries() ? 'statGood' : 'statWarning'"></span>
    </div>
</template>

<script>
    export default {
        name: 'SliderComponent',
        props: {
            'title': String,
            'value': String,
            'unit': String,
            'boundaries': Object
        },
        methods: {
            checkBoundaries() {
                return this.value <= this.boundaries.max && this.value >= this.boundaries.min ? true : false
            }
        }
    }
</script>

<style scoped>
    .slider {
        padding: 10px;
    }

    .indicator {
        display: inline-block;
        height: 1rem;
        width: 1rem;
        margin-left: 10px;
        box-sizing: border-box;
        border: 1px solid var(--black);
        border-radius: 0.35rem;
    }

    .statGood {
        background-color: var(--statGood);
    }

    .statWarning {
        background-color: var(--statWarning);
    }
</style>
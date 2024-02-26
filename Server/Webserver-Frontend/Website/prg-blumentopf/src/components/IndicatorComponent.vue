<template>
    <div class="indicator-container">
        <span class="indicator"
        :class="{statGood: isGood(), statWarning: isWarning()}"
        :style="{'background-image': 'url(' + url + ')'}"></span>
        <div v-if="data.log.length > 0">
            <p>{{ data.log[data.log.length - 1] }} {{ data.unit }}</p>
            <p>Min: {{ boundaries.min }} // Max: {{ boundaries.max }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'IndicatorComponent',
        props: {
            'data': Object,
            'boundaries': Object,
            'url': String
        },
        methods: {
            isGood() {
                return this.data.status === 'Okay' ? true : false
            },
            isWarning() {
                return this.data.status === 'Warning' ? true : false
            }
        }
    }
</script>

<style scoped>

    .indicator-container {
        text-align: center;
    }

    .indicator {
        display: inline-block;
        height: 100px;
        width: 100px;
        background-size: contain;
        box-sizing: border-box;
        border: 2px solid var(--black);
        border-radius: 0.5rem;
    }

    .statGood {
        background-color: var(--statGood);
    }

    .statWarning {
        background-color: var(--statWarning);
    }
</style>
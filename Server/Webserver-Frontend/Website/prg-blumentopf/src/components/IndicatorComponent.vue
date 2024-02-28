<!-- Vue component for status indicators on home page -->

<template>
    <div class="indicator-container">
        <!-- setting background color and image depending on sensor status and type -->
        <span class="indicator"
        :class="{statGood: isGood(), statWarning: isWarning()}"
        :style="{'background-image': 'url(' + url + ')'}"></span>
        <!-- Showing momentary value and profile boundaries, if there's data in log -->
        <div v-if="data.log.length > 0">
            <p>Status: {{ getStatus() }}</p>
            <p>Messwert: {{ data.log[data.log.length - 1] }} {{ data.unit }}</p>
            <p>Sollwert: {{ boundaries.min }} {{ data.unit }} - {{ boundaries.max }} {{ data.unit }}</p>
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
            // methods for assigning classes
            isGood() {
                return this.data.status === 'Okay' ? true : false
            },
            isWarning() {
                return this.data.status === 'Warning' ? true : false
            },
            getStatus() {
                if(this.data.status === 'Okay') {
                    return 'Okay'
                }
                if(this.data.status === 'Warning') {
                    return 'Warnung'
                }
            }
        }
    }
</script>

<style scoped>

    .indicator-container {
        text-align: center;
        padding-top: 10px;
    }

    .indicator {
        display: inline-block;
        height: 150px;
        width: 150px;
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
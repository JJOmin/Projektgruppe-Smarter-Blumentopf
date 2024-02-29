<!-- Vue component for status indicators on home page -->

<template>
    <div class="indicator-container">
        <!-- setting background color and image depending on sensor status and type -->
        <span class="indicator"
        :class="{'stat-good': isGood(), 'stat-warning': isWarning()}"
        :style="{'background-image': 'url(' + url + ')'}"></span>
        <!-- Showing momentary value and profile boundaries, if there's data in log -->
        <div v-if="data.log.length > 0">
            <p>Status: <b>{{ getStatus() }}</b></p>
            <p>Messwert: <b>{{ data.log[data.log.length - 1] }} {{ data.unit }}</b></p>
            <p>Sollwert: <b>{{ boundaries.min }} {{ data.unit }} - {{ boundaries.max }} {{ data.unit }}</b></p>
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
        padding-top: 10px;
        text-align: center;
    }

    .indicator {
        display: inline-block;
        width: 150px;
        height: 150px;
        background-size: contain;
        border: 2px solid var(--black);
        border-radius: 0.5rem;
        box-sizing: border-box;
    }

    .stat-good {
        background-color: var(--statGood);
    }

    .stat-warning {
        background-color: var(--statWarning);
    }

    @media only screen and (min-width: 576px) {
        .indicator {
            width: 200px;
            height: 200px;
        }

        .indicator-container {
            padding-top: 20px;
        }
    }

    @media only screen and (min-width: 768px) {
        .indicator {
            width: 150px;
            height: 150px;
        }
    }

</style>
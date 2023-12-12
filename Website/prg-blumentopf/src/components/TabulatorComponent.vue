<template>
    <div class="tabulator">
        <div class="tabHeaders">
            <span
                v-for="sensor in sensors"
                :key="sensor.id"
                @click="setActive(sensor.name)"
                class="tabHeader"
                :class="{activeHeader: sensor.name === isActive}">
            
                {{ sensor.name }}
            </span>
        </div>
        <div class="tabContent">
            <p>
                {{ activeTab.name }} in {{ activeTab.unit }}
                <br>Log: {{ activeTab.log }}
            </p>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'TabulatorComponent',
        props: {
            sensors: Array
        },
        data() {
            return {
                isActive: "Temperatur"
            }
        },
        methods: {
            setActive(activeTab) {
                this.isActive = activeTab
            }
        },
        computed: {
            activeTab() {
                return Object.values(this.sensors).filter((sensor) => sensor.name === this.isActive)[0]
            }
        }
    }
</script>

<style scoped>
    .tabulator {
        margin: 0 10px;
        border-radius: 5px;
        box-shadow: 0px 5px 5px var(--primaryAlt);
    }

    .tabHeaders {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .tabHeader {
        border: 1px solid var(--black);
        border-radius: 5px 5px 0 0;
        background-color: var(--primaryAlt);
        width: 33.33%;
        box-sizing: border-box;
        text-align: center;
        font-size: 0.8rem;
        padding: 4px 0;
    }

    .activeHeader {
        background-color: var(--primary);
        border-bottom-color: var(--primary);
    }

    .tabContent {
        background-color: var(--primary);
        border: 1px solid var(--black);
        border-top: none;
        border-radius: 0 0 5px 5px;
        padding: 10px;
    }

    .tabContent p {
        margin: 0;
        padding: 50px 10px;
        text-align: center;
        background-color: var(--secondaryAlt);
        border-radius: 5px;
    }
</style>
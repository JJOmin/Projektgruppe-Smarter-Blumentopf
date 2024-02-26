<template>
    <div class="settings">
    </div>
</template>

<script>
    export default {
        name: 'SettingsComponent',
        props: {
            plant: String,
            potName: String,
            profiles: Object
        },
        data() {
            return {
                selectedPlant: this.plant ? this.plant : "",
                newName: this.potName ? this.potName : ""
            }
        },
        methods: {
            updatePlant(newPlant) {
                this.$emit('updatePlant', newPlant)
            },
            updateName() {
                this.$emit('updateName', this.newName)
            }
        }
    }
</script>

<style scoped>
    .settings {
        top: 0;
        position: fixed;
        background-color: var(--secondary);
        height: 100%;
        width: 100%;
    }

    .active {
        background-color: var(--primary);
    }
</style>
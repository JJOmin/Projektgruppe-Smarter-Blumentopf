<template>

    <CardComponent>
        <HeaderComponent title="Profiles" cardHeader=True />
        <TableComponent title="Default Profiles" :profiles="defaultProfiles" @setProfile="setProfile" />
        <TableComponent title="User Profiles" :profiles="userProfiles" @setProfile="setProfile" @createProfile="createProfile" @deleteProfile="deleteProfile" />
    </CardComponent>

</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'
import TableComponent from '../components/TableComponent.vue'

export default {
    name: 'ProfilesPage',
    components: {
        CardComponent,
        HeaderComponent,
        TableComponent
    },
    props: ['defaultProfiles', 'userProfiles'],
    methods: {
        setProfile(profile) {
            this.$emit('setProfile', profile)
        },
        deleteProfile(profile) {
            this.$emit('deleteProfile', profile)
        },
        createProfile(profile) {
            this.$emit('createProfile', profile)
        }
    },
}
</script>

<style scoped>

</style>
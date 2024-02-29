<!-- Vue component for Profiles page -->

<template>

    <div class="profiles-wrapper">
        <!-- profiles as list for smaller devices (mobiles & tablets) -->
        <CardComponent class="profile-lists">
            <HeaderComponent title="Profile" cardHeader=True />
            <ListComponent title="Standard" :profiles="defaultProfiles" @setProfile="setProfile" /> <!-- List with default profiles -->
            <ListComponent title="Nutzer" :profiles="userProfiles" @setProfile="setProfile" @createProfile="createProfile" @deleteProfile="deleteProfile" /> <!-- List with user profiles -->
        </CardComponent>
        <!-- profiles as list for bigger devices (bigger tablets & Computers) -->
        <CardComponent class="profile-tables">
            <HeaderComponent title="Profile" cardHeader=True />
            <TableComponent title="Standard" :profiles="defaultProfiles" @setProfile="setProfile" /> <!-- table with default profiles -->
            <TableComponent title="Nutzer" :profiles="userProfiles" @setProfile="setProfile" @createProfile="createProfile" @deleteProfile="deleteProfile" /> <!-- table with user profiles -->
        </CardComponent>
    </div>

</template>

<script>

import CardComponent from '../components/CardComponent.vue'
import HeaderComponent from '../components/HeaderComponent.vue'
import TableComponent from '../components/TableComponent.vue'
import ListComponent from '../components/ListComponent.vue'

export default {
    name: 'ProfilesPage',
    components: {
        CardComponent,
        HeaderComponent,
        TableComponent,
        ListComponent
    },
    props: ['defaultProfiles', 'userProfiles'],
    methods: {
        // Event for selecting a Profile
        setProfile(profile) {
            this.$emit('setProfile', profile)
        },
        // Event for deleting Profile
        deleteProfile(profile) {
            this.$emit('deleteProfile', profile)
        },
        // Event for creating a new Profile
        createProfile(profile) {
            this.$emit('createProfile', profile)
        }
    },
}
</script>

<style scoped>

.profiles-wrapper {
    display: flex;
}

.profile-tables {
    display: none;
}

@media only screen and (min-width: 768px) {
    
    .profile-lists {
        display: none;
    }

    .profile-tables {
        display: block;
    }
}

</style>
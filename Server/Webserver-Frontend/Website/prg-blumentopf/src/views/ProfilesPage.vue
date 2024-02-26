<template>

    <CardComponent>
        <HeaderComponent title="Profiles" cardHeader=True />
        <TableComponent title="Default Profiles" :profiles="defaultProfiles" />
        <TableComponent title="User Profiles" :profiles="userProfiles" />
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
    props: ['defaultProfiles', 'userProfiles']
}
</script>

<style scoped>

</style>
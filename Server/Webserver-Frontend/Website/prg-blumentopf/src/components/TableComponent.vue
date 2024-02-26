<template>

    <div>
        <table>
            <tr>
                <th>{{ title }}</th>
            </tr>
            <tr>
                <th rowspan="2">Name</th>
                <th colspan="2">Temperatur</th>
                <th colspan="2">Licht</th>
                <th colspan="2">Bodenfeuchtigkeit</th>
                <th rowspan="2">Auswahl</th>
            </tr>
            <tr>
                <th>min</th>
                <th>max</th>
                <th>min</th>
                <th>max</th>
                <th>min</th>
                <th>max</th>
            </tr>
            <tr v-for="(profile, index) in profiles" :key="index">
                <td>{{ profile.name }}</td>
                <td>{{ profile.boundaries.temperature.min }}</td>
                <td>{{ profile.boundaries.temperature.max }}</td>
                <td>{{ profile.boundaries.light.min }}</td>
                <td>{{ profile.boundaries.light.max }}</td>
                <td>{{ profile.boundaries.moisture.min }}</td>
                <td>{{ profile.boundaries.moisture.max }}</td>
                <td><button>Profil auswählen</button></td>
            </tr>
        </table>
    </div>

</template>

<script>

  export default {
    name: 'TableComponent',
    props: {
      title: String,
      profiles: Object
    }
  }

</script>

<style scoped>

table {
    margin: 10px;
}

</style>
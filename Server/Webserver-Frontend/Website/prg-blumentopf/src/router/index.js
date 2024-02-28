// Vue router settings

// Imports
import { createRouter, createWebHashHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import DetailsPage from '../views/DetailsPage.vue'
import ProfilesPage from '../views/ProfilesPage.vue'
import SettingsPage from '../views/SettingsPage.vue'
import NotFound from '../views/NotFound.vue'

// Routes
const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
        props: {sensorData: Object, profileData: Object}
    },
    {
        path: '/Details',
        name: 'Details',
        component: DetailsPage,
        props: {sensorData: Object, timeStamps: Object}
    },
    {
        path: '/Profiles',
        name: 'Profiles',
        component: ProfilesPage,
        props: {defaultProfiles: Object, userProfiles: Object}
    },
    {
        path: '/Settings',
        name: 'Settings',
        component: SettingsPage,
        props: {potName: Object}
    },
    // CatchAll (error 404)
    {
        path: '/:catchAll(.*)',
        name: 'NotFound',
        component: NotFound
    }
]

// Initialize router
const router = createRouter({
    base: process.env.BASE_URL,
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router
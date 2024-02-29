<!-- Vue component for graphical visualization of sensor data on details page -->

<template>

    <div class="graph-container">
        <Line class="graph" :options="chartOptions" :data="chartData" />
    </div>

</template>

<script>
    // Imports
    import { Line } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, PointElement, LineElement, CategoryScale, LinearScale } from 'chart.js'

    ChartJS.register(Title, Tooltip, PointElement, LineElement, CategoryScale, LinearScale)

    export default {
        name: 'GraphComponent',
        components: {
            Line
        },
        props: {
            log: Array,
            timeStamps: Object
        },
        data() {
            return {
                chartData: {
                    labels: this.limitArray(this.timeStampsToArray()), // x values (timestamps from JSON) -- are not displayed
                    datasets: [{
                        tension: 0.2, // curving of the lines
                        backgroundColor: '#ffffff', // point color
                        borderColor: '#415b39', // line color
                        pointRadius: 6, // point size
                        pointHoverRadius: 9, // active point size
                        pointHitRadius: 12, // clickable point size
                        data: this.limitArray(this.log) // y values (sensor log from JSON)
                    }]
                },
                chartOptions: {
                    responsive: true,
                    scales: {
                        // Styling of the y-axis
                        y: {
                            grid: {
                                color: '#888888'
                            },
                            border: {
                                dash: [5, 10]
                            },
                            ticks: {
                                color: '#000000'
                            }
                        },
                        // Styling of the x-axis
                        x: {
                            grid: {
                                display: false
                            },
                            border: {
                                display: false
                            },
                            ticks: {
                                display: false,
                            }
                        }
                    }
                }
            }
        },
        methods: {
            // converting timestamp data to array
            timeStampsToArray() {
                let res = []
                for(let i in this.timeStamps) {
                    let stamp = this.timeStamps[i]
                    let time = this.formatValue(stamp['hour']) + ':' + this.formatValue(stamp['minute'])
                    let date = this.formatValue(stamp['day']) + '-' + this.formatValue(stamp['month']) + '-' + stamp['year']
                    let stampString = date + ' // ' + time
                    res.push(stampString)
                }
                return res
            },
            // adding leading zero where required
            formatValue(value) {
                value = value.toString()
                if(value.length == 1) {
                    return '0' + value
                } else {
                    return value
                }
            },
            // limit array max. to 10 values
            limitArray(array) {
                let newLen = 10
                if (array.length > newLen) {
                    return array.slice(-1 * newLen)
                } else {
                    return array
                }
            }
        }
    }
</script>

<style scoped>

    .graph-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.8rem;
        text-align: center;
    }
    
</style>
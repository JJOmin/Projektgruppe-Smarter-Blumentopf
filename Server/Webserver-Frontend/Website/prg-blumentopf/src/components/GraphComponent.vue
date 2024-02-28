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
                    labels: this.timeStampsToArray(), // x values (timestamps from JSON)
                    datasets: [{
                        tension: 0.2, // curving of the lines
                        backgroundColor: '#ffffff', // background color
                        borderColor: '#000000', // color of the lines
                        data: this.log // y values (sensor log from JSON)
                    }]
                },
                chartOptions: {
                    responsive: true,
                    scales: {
                        // Styling of the x & y grid
                        y: {
                            grid: {
                                color: '#000000'
                            },
                            border: {
                                dash: [5, 10]
                            },
                            ticks: {
                                color: '#ffffff'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            },
                            border: {
                                display: false
                            },
                            ticks: {
                                color: '#ffffff'
                            }
                        }
                    }
                }
            }
        },
        methods: {
            // generating test array for x values while timestamps are unavailable
            createArray(len) {
                let res = []
                for(let i = 0; i < len; i++) {
                    res.push(i)
                }
                return res
            },
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
            formatValue(value) {
                value = value.toString()
                if(value.length == 1) {
                    return '0' + value
                } else {
                    return value
                }
            }
        }
    }
</script>

<style scoped>

    .graph-container {
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
</style>
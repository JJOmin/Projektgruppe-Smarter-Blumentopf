<template>

    <div class="graph-container">
        <Line class="graph" :options="chartOptions" :data="chartData" />
    </div>

</template>

<script>
    import { Line } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, PointElement, LineElement, CategoryScale, LinearScale } from 'chart.js'

    ChartJS.register(Title, Tooltip, PointElement, LineElement, CategoryScale, LinearScale)

    export default {
        name: 'GraphComponent',
        components: {
            Line
        },
        props: {
            log: Array
        },
        data() {
            return {
                chartData: {
                    labels: this.createArray(this.log.length),
                    datasets: [{
                        tension: 0.2,
                        backgroundColor: '#ffffff',
                        borderColor: '#000000',
                        data: this.log
                    }]
                },
                chartOptions: {
                    responsive: true,
                    scales: {
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
            createArray(len) {
                let res = []
                for(let i = 0; i < len; i++) {
                    res.push(i)
                }
                return res
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
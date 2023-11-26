from SoilSensor import SoilSensor



class AllSensors: #Class that holds instances of every sensor to get measurments
    def __init__(self, soilData):
        self.soilData = soilData
        soilSensor = SoilSensor(soilData)
        self.soilSensorReading = 'no data'
        self.lightSensorReading = 'no data'
        self.temperaturSensorReading = 'no data'
        
    def get():
        return 
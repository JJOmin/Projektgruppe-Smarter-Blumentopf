from SoilSensor import SoilSensor



class AllSensors: #Class that holds instances of every sensor to get measurments
    def __init__(self, soilData):
        self.soilData = soilData
        soilSensor = SoilSensor(soilData)
        
        
        self.soilSensorValue = 'no data'
        self.lightSensorValue = 'no data'
        self.temperaturSensorValue = 'no data'
        
    def readSoilSensor():
        self.soilSensorValue = soilSensor.read_moisture()
from SoilSensor import SoilSensor
from TemperatureSensor import TemperatureSensor
from LightSensor import LightSensor



class AllSensors: #Class that holds instances of every sensor to get measurments
    def __init__(self, soilData, tempData, lightData):
        self.soilData = soilData #datenvariable fuer den Bodensensor
        self.tempData = tempData #datenvariable fuer den Temperatursensor
        self.lightData = lightData #datenvariable fuer den Lichtsensor
        
        #Instanzierung der Sensor-Klassen
        self.soilSensor = SoilSensor(soilData)
        self.temperatureSensor = TemperatureSensor(tempData)
        self.lightSensor = LightSensor(lightData) 
    
        #Erstellung Sensor Daten Eingenschaften
        self.soilSensorValue = 'no data'
        self.lightSensorValue = 'no data'
        self.temperaturSensorValue = 'no data'
        
        
    def readSoilSensor(self):
        self.soilSensorValue = self.soilSensor.readMoisture()
        
    def readTemperatureSensor(self):
        self.temperaturSensorValue = self.temperatureSensor.readTemperature()
        
    def readLightSensor(self):
        self.lightSensorValue = self.lightSensor.readLightSensor()
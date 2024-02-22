#from SoilSensor import SoilSensor
from TemperatureSensor import TemperatureSensor
from LightSensor import LightSensor
from SoilSensor import SoilSensor


class AllSensors: #Class that holds instances of every sensor to get measurments
    def __init__(self, soilData, tempData, lightData):
        self.soilData = soilData # datenvariable fuer den Bodensensor
        self.tempData = tempData #datenvariable fuer den Temperatursensor
        self.lightData = lightData #datenvariable fuer den Lichtsensor
        
        #Instanzierung der Klassen???
        #self.soilSensor = SoilSensor(soilData)
        self.temperatureSensor = TemperatureSensor(tempData)
        self.lightSensor = LightSensor(lightData) 
        
        self.soilSensorValue = 'no data' # Die Variable soll einfach keine daten haben damit die später überschireben werden können mit den Sensor daten? 
        self.lightSensorValue = 'no no no no data'
        self.temperaturSensorValue = 'no data'
        
        
    def readAll(self):
        #self.soilSensorValue = self.soilSensor.readSoilSensor()
        #if self.soilSensorValue != None:#wenn nicht None returnt wird (passiert wenn die letzte Messung nicht mindestens measureDuration (z.b. 5000 ms) her ist)
            #print("Bodenfeuchtigkeit:", self.soilSensorValue)
        self.temperaturSensorValue = self.temperatureSensor.readTemperature() #Hier auslese der read klasse also ne methode die inszanziert in dieser klasse
        self.lightSensorValue = self.lightSensor.readLightSensor(0x20)
        #print("Light:", self.lightSensorValue)
        return [0, self.temperaturSensorValue, self.lightSensorValue] #self.soilSensorValue
        
        
    def readSoilSensor(self):
        #self.soilSensorValue = self.soilSensor.readSoilSensor()
        print("Test")
        
    def readTemperatureSensor(self):
        self.temperaturSensorValue = self.temperatureSensor.readTemperature() #Hier auslese der read klasse also ne methode die inszanziert in dieser klasse
        
    def readLightSensor(self):
        self.lightSensorValue = self.lightSensor.readLightSensor(0x20)
        
        
        
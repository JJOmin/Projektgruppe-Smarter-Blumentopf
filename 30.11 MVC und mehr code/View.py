#View
from AllSensors import AllSensors
from Display import Display

class View:
    def __init__(self, allSensors):
        self.allSensors = allSensors
        self.display = Display()
        
    
    def printAllData(self): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion
        self.allSensors.readTemperatureSensor()
        self.allSensors.readSoilSensor()
        self.allSensors.readLightSensor() # der sensor geht noch nicht
        avg_percentage, _  = self.allSensors.soilSensorValue  # toupel auseinander nehmen 
        self.display_text = "Bodenfreuchtigkeit:" + str(avg_percentage) + "%:Temperatur:" + str(self.allSensors.temperaturSensorValue) + "°C:Licht:" + str(self.allSensors.lightSensorValue)+"lux:"
        self.display.update_display_text(self.display_text)
        self.display.display_updated_text() 
    
    
    
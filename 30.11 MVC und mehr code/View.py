#View
from Controller import Controller
from AllSensors import AllSensors
from Display import Display

class View:
    def __init(self, viewData)
    self.viewData = viewData
    self.display = Display()
    
    def printAllData(): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion
        self.allSensors.readTemperatureSensor()
        self.allSensors.readSoilSensor()
        self.allSensors.readLightSensor() # der sensor geht noch nicht
        avg_percentage, _  = self.allSensors.soilSensorValue  # toupel auseinander nehmen 
        display_text = "Bodenfreuchtigkeit:" + str(avg_percentage) + "%:Temperatur:" + str(self.allSensors.temperaturSensorValue) + "°C:Licht:" + str(self.allSensors.lightSensorValue)+"lux:"
        display.update_display_text(display_text)
        display.display_updated_text() 
        pass
    
    
    
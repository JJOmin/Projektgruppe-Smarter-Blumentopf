#View
from Controller import Controller
from AllSensors import AllSensors


class View:
    def __init(self, viewData)
    self.viewData= viewData
    
    def printAllData(): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion
        self.allSensors.readTemperatureSensor()
        self.allSensors.readSoilSensor()
        self.allSensors.readLightSensor() # der sensor geht noch nicht
        pass
    
    
    
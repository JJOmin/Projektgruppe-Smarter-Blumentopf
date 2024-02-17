#View
#from AllSensors import AllSensors
#from Model import Model
from Display import Display

class View:
    def __init__(self, model):
       # self.allSensors = allSensors
        self.model = model
        self.display = Display()
        
    def printAllData(self): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion
#        self.allSensors.readTemperatureSensor()
#        self.allSensors.readSoilSensor()
#        self.allSensors.readLightSensor() # der sensor geht noch nicht
#        self.avg_percentage = self.allSensors.soilSensorValue[0]  # toupel auseinander nehmen
        display_text = "Bodenfeuchtigkeit:" + str(self.model.currentValues['moisture']) + "%:Temperatur:" + str(self.model.currentValues['temperature']) + chr(0)+"C:Licht:" + str(self.model.currentValues['light'])+"lux:"

        #print(display_text)
        self.display.update_display_text(display_text)
        self.display.display_updated_text()
        
    # HIT Demo
    #def printAllDataDemo(self): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion
        #display_text = "Feuchtigkeit:" + str(self.model.currentValues['moisture']) + "%:Temperatur:" + str(self.model.currentValues['temperature']) + chr(0)+"C:Licht:" + str(self.model.currentValues['light'])+"lux:"

        #self.display.update_display_text(display_text)
        #self.display.display_updated_text() 
    
    
    

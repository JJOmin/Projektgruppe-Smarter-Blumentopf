#View
from Display import Display

class View:
    def __init__(self, model):
        self.model = model
        self.display = Display()
        
    def printAllData(self): #Methode nur fuer Programmierer, zum ueberpruefen der daten funktion

        display_text = "Feuchtigkeit:" + str(self.model.currentValues['moisture']) + "%:Temperatur:" + str(self.model.currentValues['temperature']) + chr(0)+"C:Licht:" + str(self.model.currentValues['light'])+"lux:"

        self.display.update_display_text(display_text)
        self.display.display_updated_text()
    
    
    

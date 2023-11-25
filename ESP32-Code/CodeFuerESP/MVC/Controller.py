#Controller

from Temperatur import Temperatur
from BodenfeutikeitsSensor import Bodenfeuchtigkeitsensor

class Controller:
    def __init__(self, beispiel):
        self.beispiel= beispiel
        
    def beispiel_methode(self):
        print(self.beispiel)
        
    def start_Sensor_by_press():
        
#Instanzierung
controller_instanz = Controller(5)
controller_instanz.beispiel_methode()
        

    
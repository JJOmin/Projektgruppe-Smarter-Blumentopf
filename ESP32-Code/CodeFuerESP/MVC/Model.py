# Modell

from Controller import Controller

class Model(Controller):
    def __init__(self, beispiel, beispielNeu):
        super().__init__(beispiel) # Aufruf der klasse controller
        self.beispielNeu = beispielNeu
        
    def beispielNeu_methode(self):
        print(self.beispielNeu)
        self.beispiel_methode() # ruft hier die vererbte methode Vom controller auf 
        
model_instanz = Model(10,20)
model_instanz.beispielNeu_methode()
# der obere code ist nur ein Beispiel wie vererbung auf dem ESP32 funktionieren kann
# Beachte hierbei das die klasse Controller.py auf dem Controller gespeichert werden muss!!!  
    
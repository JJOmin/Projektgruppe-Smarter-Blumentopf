#Controller

class Controller:
    def __init__(self, beispiel):
        self.beispiel= beispiel
        
    def beispiel_methode(self):
        print(self.beispiel)
        
#Instanzierung
controller_instanz = Controller(5)
controller_instanz.beispiel_methode()
        

    
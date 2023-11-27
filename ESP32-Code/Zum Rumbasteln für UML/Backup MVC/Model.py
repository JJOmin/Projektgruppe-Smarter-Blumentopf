# Modell

#from Controller import Controller

class Model:
    def __init__(self):
        self.ssid = "Flat mars society 5G death laser"
        self.wifiPw = "5G power"
        self.remoteUrl = 'https://www.tilly.cloud/Blumentopf/Database/plantData.json'  # falls fehler auftrete auf "https://cloudleo.duckdns.org/Blumentopf/Database/daten.json" setzen
        self.uploadUrl = 'https://blumentopfupload.tilly.cloud/Blumentopf/upload_data' # falls fehler auftreten auf "http://31.19.90.130:5000/Blumentopf/upload_data" setzen
        self.webUser = b'Blumentopf'
        self.webPw = b'Blumentopf_123'
        
        self.soilData = {'dpin':35, 'wet': 3842.04, 'dry': 4095, 'numValuesAvg': 2, 'measureDuration': 5000, 'numCalibrations':  4}
        self.tempData = {'dpin':22}
        self.lightData = {'scl':22, 'sda': 21}

        self.plantData = {'plantName': 0}
        
        
    def set(self, **kwargs): #sets new values into attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def get(self, attr_name): #Etwas überflüssig, aber eventuell wegen vererbung noch notwendig
        return getattr(self, attr_name)


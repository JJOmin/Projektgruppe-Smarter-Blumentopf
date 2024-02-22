# Modell
import ujson

class Model:
    def __init__(self):
        self.ssid = "Creak-Dealer Junior" #Wlan name Creak-Dealer Junior
        self.wifiPw = "hallo123" #Wlan Passwort hallo123
        self.remoteUrl = 'https://www.tilly.cloud/Blumentopf/Database/plantData.json'  # falls fehler auftrete auf "https://cloudleo.duckdns.org/Blumentopf/Database/daten.json" setzen
        self.prototypUrl = 'https://www.tilly.cloud/Blumentopf/Database/prototyp.json'
        self.profileUrl = 'https://www.tilly.cloud/Blumentopf/Database/db.json'
        self.uploadUrl = 'https://cloudleo.duckdns.org/Blumentopf/Database/api.php'
        #self.uploadUrl = 'https://blumentopfupload.tilly.cloud/Blumentopf/upload_data' # falls fehler auftreten auf "http://31.19.90.130:5000/Blumentopf/upload_data" setzen
        self.webUser = b'Blumentopf'
        self.webPw = b'Blumentopf_123'
        self.localFileName = 'profileData.json'
        
        self.soilData = {'dpin':35, 'wet': 3842.04, 'dry': 4095, 'numValuesAvg': 2, 'measureDuration': 5000, 'numCalibrations':  4}
        self.tempData = {'dpin':22}
        self.lightData = {'scl':22, 'sda': 21}
        self.btnData = {'dpin':25}
        self.ledPins = {"light": 4, "moisture": 16, "temperature": 17}
        
        self.prototypData = {}
        self.profileData = {}
        
        self.lightLog = []
        self.temperatureLog = []
        self.soilLog = []
        self.currentValues = {'light': 'not defined', 'moisture': 'not defined', 'temperature': 'not defined'}
        self.status = {'light': 'Okay', 'moisture': 'Okay', 'temperature': 'Okay'}
        #self.demoStatus = {'light': 'Okay', 'moisture': 'Okay', 'temperature': 'Okay'} # HIT Demo
        
    def set(self, **kwargs): #sets new values into attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def get(self, attr_name): #Etwas überflüssig, aber eventuell wegen vererbung noch notwendig
        return getattr(self, attr_name)
    
    def save_json_if_changed(self, filename, data):
      # Überprüfe, ob die Datei existiert, und erstelle sie, wenn nicht
        try:
            with open(filename, 'r'):
                pass
        except OSError:
    # Datei existiert nicht, erstelle eine leere Datei
            with open(filename, 'w') as file:
                ujson.dump({}, file)
                print("Leere Datei erstellt.")
        try:
        # Versuche, die vorhandene Datei zu öffnen und deren Inhalt zu lesen
            with open(filename, 'r') as file:
                current_data = ujson.load(file)
        except (OSError, ValueError):
        # Wenn die Datei nicht vorhanden oder nicht lesbar ist, setze den aktuellen Inhalt auf None
            current_data = None
  

    # Vergleiche den aktuellen Inhalt mit dem neuen Inhalt
        if current_data != data:
        # Wenn sich die Daten unterscheiden, speichere die neue JSON-Datei
            with open(filename, 'w') as file:
                ujson.dump(data, file)
            print("Daten wurden aktualisiert.")
        else:
            print("Daten sind bereits aktuell.")
        
    def load_json(self,filename):
        try:
            with open(filename, 'r') as file:
                data = ujson.load(file)
            return data
        except (OSError, ValueError):
            print(f"Fehler beim Laden der Datei '{filename}'.")
            return None


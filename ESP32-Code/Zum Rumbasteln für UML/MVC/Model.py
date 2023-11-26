# Modell

#from Controller import Controller

class Model:
    def __init__(self):
        self.ssid = "0"
        self.WifiPw = "0"
        self.remoteUrl = 'https://www.tilly.cloud/Blumentopf/Database/plantData.json'
        self.uploadUrl = 'https://blumentopfupload.tilly.cloud/Blumentopf/upload_data'
        self.webUser = b'Blumentopf'
        self.webPw = b'Blumentopf_123'
        
    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print("Variables updated successfully")
        
    def get(self, *args):
        if not args:
            return {attr: getattr(self, attr) for attr in dir(self) if not attr.startswith("__") and not callable(getattr(self, attr))}
        else:
            return {attr: getattr(self, attr) for attr in args if hasattr(self, attr)}
        
# model_instanz = Model()
# # Abrufen der Werte von allen Attributen
# print("")
# print(model_instanz.get())
# print("")
# 
# # Abrufen der Werte von spezifischen Attributen
# print(model_instanz.get('ssid'))

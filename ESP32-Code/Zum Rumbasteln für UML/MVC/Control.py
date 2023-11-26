from Server import Server
from Model import Model

class Control:
    def __init__(self):
        self.beispiel = "beispiel"
        self.model = Model()
        
        
    def serverTest(self):
        Server = Server(self.model.ssid, self.model.wifiPw, self.model.remoteUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        Server.connectWifi()
        print(Server.getRemote())
        print(Server.setTestDataToServer())
        print(Server.getRemote())
        
        
        
#Instanzierung
#control = Control()
#control.serverTest
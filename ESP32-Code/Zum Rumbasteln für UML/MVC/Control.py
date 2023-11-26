from Server import Server
from Model import Model
from AllSensors import AllSensors

class Control:
    def __init__(self):
        self.model = Model()
        
    def serverTest(self):
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.remoteUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.server.connectWifi()
        print(self.server.getRemote())
        print(self.server.setTestDataToServer())
        print(self.server.getRemote())
        
    def sensorTest(self):
        print(self.model.tempData)
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData)
        
        print(self.allSensors.soilSensorValue, self.allSensors.temperatureSensor)
        #self.allSensors.readTemperature()
        self.allSensors.readSoilSensor()
        print(self.allSensors.soilSensorValue, self.allSensors.temperatureSensor)
        

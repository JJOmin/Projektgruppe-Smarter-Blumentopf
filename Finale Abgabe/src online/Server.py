import network
import time
import urequests
import machine
import ubinascii
import json
import requests
from machine import RTC


class Server:
    def __init__(self, ssid, wifiPw, profileUrl, prototypUrl, uploadUrl, webUser, webPw):
        self.ssid = ssid #Wlan name
        self.password = wifiPw 
        self.uploadUrl = uploadUrl
        self.profileUrl = profileUrl
        self.prototypUrl = prototypUrl
        self.username = webUser
        self.password_b = webPw
        self.sta_if = network.WLAN(network.STA_IF)

        #Muss ins Model
        self.profileName = ""  #beinhaltet den namen des Aktuellen Pflanzenprofiels
        self.profileBoundaries = "" #beinhaltet alle grenzwerte für die aktuelle Planze
        self.currentPrototyp = "" #beinhaltet das gesamte Daten Log einer Pflanze um weitere daten anzuhängen
        self.currentData = "" #beinhaltet die aktuell gemessenen werte und versendet diese

    #funtkion zur verbindung mit dem Internet
    def connectWifi(self):
        
        try:
            print("Connecting to WiFi", end="")
            point = 0
            self.sta_if.active(True)
            self.sta_if.connect(self.ssid, self.password)
            while not self.sta_if.isconnected(): #and point < 20: #TestMemo ab dem and
                print(".", end="")
                time.sleep(0.1)
                point += 1
            if self.sta_if.isconnected():
                print(" Connected!")
            else:
                print(" Failed! No WiFi connection!")
        
        
        except Exception as e:
            print("Fehler:", e)
    #methode die auf prototyp.json zugreift
    def getPrototype(self):
        auth = 'Basic ' + ubinascii.b2a_base64(self.username + b":" + self.password_b).strip().decode('utf-8')
        headers = {'Authorization': auth}
        
        try:
            response = urequests.get(self.prototypUrl, headers=headers)
            if response.status_code == 200:
                content = response.text
                response.close()
                self.currentPrototyp = json.loads(content)
                self.profileName = json.loads(content)['selectedPlant']
                return [self.currentPrototyp, self.profileName]
            else:
                response.close()
                return None
        except Exception as e:
            print("Fehler:", e)
    
    #funktion die alle Profile auf dem Server herrunterlaed
    def getProfile(self): #returns only the profileUrl content
        auth = 'Basic ' + ubinascii.b2a_base64(self.username + b":" + self.password_b).strip().decode('utf-8')
        headers = {'Authorization': auth}
        
        try:
            response = urequests.get(self.profileUrl, headers=headers)
            print(response.text)
            if response.status_code == 200:
                content = response.text
                response.close()
                self.profileBoundaries = json.loads(content)[self.profileName]
                return [self.profileBoundaries, self.profileName]
                #if self.profileName in json.loads(content)["profiles"].keys():
                    #self.profileBoundaries = json.loads(content)["profiles"][self.profileName]
                    #return [self.profileBoundaries, self.profileName]
                #else:
                    #self.profileBoundaries = self.currentPrototyp["profiles"][self.profileName]
                    #return [self.profileBoundaries, self.profileName]
            else:
                response.close()
                return None
        except Exception as e:
            print("Fehler:", e)
            return False  # Hier wird False zurückgegeben, wenn eine Ausnahme auftritt

    #methode zum hinzufügen neuer messwerte zum array
    def addMeasurement(self, temperature, light, moisture):
        # Füge die neuen Messwerte zum Prototyp hinzu
        #self.currentPrototyp['sensors']['temperature']['log'].extend(temperature)
        #self.currentPrototyp['sensors']['light']['log'].extend(light)
        #self.currentPrototyp['sensors']['moisture']['log'].extend(moisture)
        
        self.currentData = {}
        self.currentData['temperature'] = temperature[0]
        self.currentData['light'] = light[0]
        self.currentData['moisture'] = moisture[0]
        
        date = time.localtime()
        
        year = date[0]
        month = date[1]
        day = date[2]
        hour = date[3]
        minute = date[4]
        
        timeStamp = {'year': year,
                     'month': month,
                     'day': day,
                     'hour': hour,
                     'minute': minute}
        
        #self.currentPrototyp['timeStamps'].append(timeStamp)
        
        self.currentData['timeStamp'] = timeStamp
        
        self.sendData() 
        
    def sendData(self):
        auth = 'Basic ' + ubinascii.b2a_base64(self.username + b":" + self.password_b).strip().decode('utf-8')
        headers = {'Authorization': auth}
        
        json_data = json.dumps(self.currentData)# + "}" #json.dumps(data_to_send)
        #json_data = json.dumps(["data"])
        try:
            response = requests.post(self.uploadUrl, data = json_data, headers = headers)
            if response.status_code == 200:
                print("Daten erfolgreich gesendet")
                print(json.loads(response.text)["message"])
            else:
                print("Fehler beim Senden der Daten:", response.status_code)
        except Exception as e:
            print("Fehler:", e)

    def statusPush(self, status):
        try:
            #print(self.currentPrototyp)
            for key, value in status.items():
                self.currentPrototyp['sensors'][key]['status'] = status[key]
            self.sendData() #senden von daten wenn grenzwerte überschritten wurden
            
        except Exception as e:
            print("Fehlerrrrrr:", e)

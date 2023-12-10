import network
import time
import urequests
import machine
import ubinascii
import json
import requests
from machine import RTC


class Server:
    def __init__(self, ssid, wifiPw, uploadUrl, webUser, webPw):
        self.ssid = ssid
        self.password = wifiPw
        self.upload_url = uploadUrl
        self.username = webUser
        self.password_b = webPw
        self.sta_if = network.WLAN(network.STA_IF)
        
    def connectWifi(self):
        print("Connecting to WiFi", end="")
        self.sta_if.active(True)
        self.sta_if.connect(self.ssid, self.password)
        while not self.sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)
        print(" Connected!")
    
    def getRemote(self, url): #Returns content of RemoteURL
        auth = 'Basic ' + ubinascii.b2a_base64(self.username + b":" + self.password_b).strip().decode('utf-8')
        headers = {'Authorization': auth}
        
        response = urequests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.text
            response.close()
            return content
        else:
            response.close()
            return None
    
    def get_date(self): #Returns Date and Time
        rtc = RTC()
        datetime = rtc.datetime()
        year, month, day, _, hour, minute, second, _ = datetime
        date_str = "{0:04d}-{1:02d}-{2:02d}".format(year, month, day)
        time_str = "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)
        return [date_str, time_str]
    
    def setTestDataToServer(self): #Sets a Test value into the json File on upload path
        date_time = self.get_date()
        data = {
            "TEST-DATA": "Data Test",
            "Datum": date_time[0],
            "Uhrzeit": date_time[1],
            
        }
        response = requests.post(self.upload_url, json=data)
        if response.status_code == 200:
            return "Daten erfolgreich gesendet und gespeichert."
        else:
            return f"Fehler beim Senden der Daten: {response.status_code}"
        
    def setUpload(self, content):
        date_time = self.get_date()
        data = {
            "Temperatur": content[0],
            "Bodenfeuchtigkeit": content[1],
            "Helligkeit": content[2],
            "Datum": date_time[0],
            "Uhrzeit": date_time[1],
            
        }
        response = requests.post(self.upload_url, json=data)
        if response.status_code == 200:
            return "Daten erfolgreich gesendet und gespeichert."
        else:
            return f"Fehler beim Senden der Daten: {response.status_code}"

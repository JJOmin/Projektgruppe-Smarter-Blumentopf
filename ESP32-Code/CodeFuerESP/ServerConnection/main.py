import network
import time
import urequests
import machine
import ubinascii
import json
import requests
from machine import RTC


class ServerConnection:
    def __init__(self, ssid, password, remote_url, upload_url, username, password_b):
        self.ssid = ssid
        self.password = password
        self.remote_url = remote_url
        self.upload_url = upload_url
        self.username = username
        self.password_b = password_b
        self.sta_if = network.WLAN(network.STA_IF)
        
    def connect_to_wifi(self):
        print("Connecting to WiFi", end="")
        self.sta_if.active(True)
        self.sta_if.connect(self.ssid, self.password)
        while not self.sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)
        print(" Connected!")
    
    def get_remote_file_content(self):
        auth = 'Basic ' + ubinascii.b2a_base64(self.username + b":" + self.password_b).strip().decode('utf-8')
        headers = {'Authorization': auth}
        
        response = urequests.get(self.remote_url, headers=headers)
        if response.status_code == 200:
            content = response.text
            response.close()
            return content
        else:
            response.close()
            return None
    
    def get_date(self):
        rtc = RTC()
        datetime = rtc.datetime()
        year, month, day, _, hour, minute, second, _ = datetime
        date_str = "{0:04d}-{1:02d}-{2:02d}".format(year, month, day)
        time_str = "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)
        return [date_str, time_str]
    
    def set_readings_to_server(self):
        date_time = self.get_date()
        data = {
            "Datum": date_time[0],
            "Uhrzeit": date_time[1],
            
        }
        response = requests.post(self.upload_url, json=data)
        if response.status_code == 200:
            return "Daten erfolgreich gesendet und gespeichert."
        else:
            return f"Fehler beim Senden der Daten: {response.status_code}"
    
#     def main(self):
#         self.connect_to_wifi()
#         print(self.set_readings_to_server())
#         file_content = self.get_remote_file_content()
#         if file_content:
#             
#             #print('Inhalt der Datei aus', self.remote_url)
#             #print("")
#             #print("Ausgabe als convertiertes Array: ")
#             #print(json.loads(file_content))  # Konvertierung Json in Python-Array
#         else:
#             print('Fehler beim Abrufen der Datei.')


# Informationen die benötigt werden um die Klasse zu initialisieren
ssid = 'Kleiner Riese Oben'
password = 'Hola_Emden_Wifi'
remote_url = 'https://cloudleo.duckdns.org/Blumentopf/Database/daten.json'
upload_url = 'http://31.19.90.130:5000/Blumentopf/upload_data'  # Sollte noch in die Offizielle URL geändert werden, aber aktuell noch nicht freigegeben
username = b'Blumentopf'
password_b = b'Blumentopf_123'

connection = ServerConnection(ssid, password, remote_url, upload_url, username, password_b)
connection.connect_to_wifi()
print(connection.get_remote_file_content())
print(connection.set_readings_to_server())
print(connection.get_remote_file_content())


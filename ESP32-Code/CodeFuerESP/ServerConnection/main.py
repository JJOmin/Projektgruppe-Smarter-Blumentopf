import network
import time
import urequests
import machine
import ubinascii
import json
import requests
from machine import RTC



print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Kleiner Riese Oben', 'Hola_Emden_Wifi')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

# URL zur Datei auf dem entfernten Webserver
url = 'https://cloudleo.duckdns.org/Blumentopf/Database/daten.json'
url2 = 'http://31.19.90.130:5000/Blumentopf/upload_data' #Sollte noch in die Offizielle URL geändert werden, aber aktuell noch nicht freigegeben

# Benutzername und Passwort für die Basic-Authentifizierung
username = b'Blumentopf'
password = b'Blumentopf_123'

# Funktion, um Daten von der entfernten Datei abzurufen
def get_remote_file_content(url):
    auth = 'Basic ' + ubinascii.b2a_base64(username + b":" + password).strip().decode('utf-8')
    headers = {'Authorization': auth}
    
    response = urequests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.text
        response.close()
        return content
    else:
        response.close()
        return None
    
def currentTime():
    rtc = RTC()
    datetime = rtc.datetime()
    # Informationen extrahieren
    year = datetime[0]
    month = datetime[1]
    day = datetime[2]
    weekday = datetime[3]  # Wochentag (0 = Montag, 6 = Sonntag)
    hour = datetime[4]
    minute = datetime[5]
    second = datetime[6]
    array = []
    array.append(["{0:04d}-{1:02d}-{2:02d}".format(year, month, day)])
    array.append(["{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)])
    return array
    
def set_Value_Server(url2):
    # Beispiel-Daten als JSON
    print(currentTime()[0])
    data = {
        "Datum": currentTime()[0],
        "Uhrzeit": currentTime()[1]
    }
    # Senden der POST-Anfrage
    response = requests.post(url2, json=data)

    # Überprüfen der Antwort
    if response.status_code == 200:
        return("Daten erfolgreich gesendet und gespeichert.")
    else:
        return("Fehler beim Senden der Daten:", response.status_code)
    

# Hauptprogramm
def main():
    print(set_Value_Server(url2))
    file_content = get_remote_file_content(url)
    if file_content:
        print('Inhalt der Datei aus', url)
        print("")
        print("Ausgabe als convertiertes Array: ")
        print(json.loads(file_content)) #Konvertierung Json in Python array
        #print(json.loads(file_content).keys())
    else:
        print('Fehler beim Abrufen der Datei.')
        
main()

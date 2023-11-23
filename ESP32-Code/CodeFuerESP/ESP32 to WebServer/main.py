import network
import time
import urequests
import machine
import ubinascii
import json

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Kleiner Riese Oben', 'Hola_Emden_Wifi')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

# URL zur Datei auf dem entfernten Webserver
url = 'https://cloudleo.duckdns.org/Blumentopf/daten.json'

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

# Hauptprogramm
def main():
    file_content = get_remote_file_content(url)
    if file_content:
        print("")
        print('Inhalt der Datei aus', url)
        print(file_content)
        print("")
        print("Ausgabe als convertiertes Array: ")
        print(json.loads(file_content)) #Konvertierung Json in Python array
        #print(json.loads(file_content).keys())
    else:
        print('Fehler beim Abrufen der Datei.')
        
main()

import network
import time
import urequests
import machine
import ubinascii
import requests
import json

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")



url = 'http://31.19.90.130:5000/Blumentopf/upload_data'  # Ihre Server-IP-Adresse hier einsetzen
print("vorläufige URL")

# Beispiel-Daten als JSON
data = {
    "sensor": "DHT22",
    "temperature": 25.4,
    "humidity": 60.2
}

# Senden der POST-Anfrage
response = requests.post(url, json=data)

# Überprüfen der Antwort
if response.status_code == 200:
    print("Daten erfolgreich gesendet und gespeichert.")
else:
    print("Fehler beim Senden der Daten:", response.status_code)

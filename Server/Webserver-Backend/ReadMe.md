# Dokumentation: Einrichtung und Starten von Python Flask im Venv

1. Auf das Venv auf dem Server in dem Python mit Flask läuft zugreifen: 
```bash
bash:
source myflaskenv/bin/activate
```
2. App.py im venv starten:
```bash
bash:
gunicorn -w 4 -b 192.168.178.59:5000 app:app
```
3. Beenden über Control + C

4. Verlassen von venv:

```bash
bash:
deactivate
```
6. Auf app.py zugreifen im venv:
```bash
bash
nano app.py
```
(Speichern in Nano mit Control + X und dann Y, Enter)

7. Code der app.py für Flask auf dem Server:
```python
Python:
from flask import Flask, request
import json
import datetime

app = Flask(__name__)

@app.route('/Blumentopf/upload_data', methods=['POST'])
def upload_data():
    if request.method == 'POST':
        try:
            data = request.get_json()  # JSON-Daten von ESP32 erhalten
            if data:  # Überprüfen, ob gültige JSON-Daten erhalten wurden
                current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f'/var/www/blumentopfbackend/Database/received_data_{current_time}.json'  # Speicherort und Dateiname
                with open(file_name, 'w') as file:  # Daten in eine neue Datei schreiben
                    json.dump(data, file, indent=4)
                return "Daten erfolgreich empfangen und gespeichert"
            else:
                return "Ungültige JSON-Daten erhalten"
        except Exception as e:
            return f"Fehler beim Verarbeiten der Daten: {str(e)}"
    else:
        return "Nur POST-Anfragen erlaubt"

if __name__ == '__main__':
    app.run(host='192.168.178.59', port=5000)  # Anpassen des Ports und der Host-Adresse nach Bedarf
```

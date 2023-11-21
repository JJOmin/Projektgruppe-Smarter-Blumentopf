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
                file_path = '/var/www/Blumentopf/Database/input/'
                file_name = f'received_data_{current_time}.json'  # Eindeutiger Dateiname
                with open(file_path + file_name, 'w') as file:  # Daten in eine neue Datei schreiben
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

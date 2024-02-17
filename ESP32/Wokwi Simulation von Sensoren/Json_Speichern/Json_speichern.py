import ujson

def save_json_if_changed(filename, data):
      # Überprüfe, ob die Datei existiert, und erstelle sie, wenn nicht
    try:
        with open(filename, 'r'):
            pass
    except OSError:
    # Datei existiert nicht, erstelle eine leere Datei
        with open(filename, 'w') as file:
            ujson.dump({}, file)
            print("Leere Datei erstellt.")
    try:
        # Versuche, die vorhandene Datei zu öffnen und deren Inhalt zu lesen
        with open(filename, 'r') as file:
            current_data = ujson.load(file)
    except (OSError, ValueError):
        # Wenn die Datei nicht vorhanden oder nicht lesbar ist, setze den aktuellen Inhalt auf None
        current_data = None
  

    # Vergleiche den aktuellen Inhalt mit dem neuen Inhalt
    if current_data != data:
        # Wenn sich die Daten unterscheiden, speichere die neue JSON-Datei
        with open(filename, 'w') as file:
            ujson.dump(data, file)
        print("Daten wurden aktualisiert.")
    else:
        print("Daten sind bereits aktuell.")
        
def load_json(filename):
    try:
        with open(filename, 'r') as file:
            data = ujson.load(file)
        return data
    except (OSError, ValueError):
        print(f"Fehler beim Laden der Datei '{filename}'.")
        return None


# Beispielverwendung:
filename = 'example.json'

loaded_data = load_json(filename)

if loaded_data is not None:
    print("Geladene Daten:", loaded_data)
else:
    print("Fehler beim Laden der Daten.")

new_data = {'key': 'value', 'number': 47}

# Jetzt kannst du die Funktion aufrufen
save_json_if_changed(filename, new_data)


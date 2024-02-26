# Programmablauf ESP32

## Setup
    - MVC Initialisierung
    - Aufbau der Wifi Connection
    - JSON Daten vom Server laden (db.json & prototyp.json) --> im Model speichern

## Programm-Loop (60 mal die Sekunde)

### Sensoren Intervall (alle 5 Sekunden)
    - Lesen der Sensorwerte
    - Vergleichen mit den Grenzwerten des gewählten Profils
        - ggfs. Status ändern --> Status Change Function (siehe unten)
    - Speichern der Messwerte im Model
        
### Server Intervall (nach 5 gemessenen Werte)
    - JSON Daten vom Server laden (prototyp.json) --> im Model speichern
        - ggfs. Änderungen für Name & Profil übernehmen
            - Bei Profiländerung: Neues Profil aus der db.json laden & Grenzwerte aktualisieren
    - Messwerte des Sensoren Intervalls mitteln
    - gemittelte Werte dem Log in der "prototyp.json" anhängen
    - "prototyp.json" auf dem Server überschreiben
    - Messwerte des Sensor Intervalls im Model zurücksetzen
    
### Button Pressed?
    - Wenn der Button gedrückt wird: Ausgabe der aktuellen Werte auf dem Display
    
### Status Change
    - LEDs Aktivieren/Deaktivieren
    - ggfs. Pumpe für kurze Zeit aktivieren
    - JSON Daten vom Server laden (prototyp.json)
    - Status in "prototyp.JSON" ändern
    - "prototyp.json" auf dem Server überschreiben
    

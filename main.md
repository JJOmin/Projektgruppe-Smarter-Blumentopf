# setup
    - MVC initialisierung(JSON Data)
    - wifi connection
    - JSON Data from server
    
    - (set starttime)

# loop (60 mal die Sekunde)


## Sensoren Intervall (alle 5-10 sekunden)
    - Lesen der Sensoren
    - Prüfen grenzwerte
        - Falls Kritisch -> Pumpe & Status Change
    - Schreiben werte in Model (in ZyklusArray)
        
## Server Intervall (alle 90 Sek für demo sonst 15-30 Minuten)
    - Json Lesen Server -> in Model (prototyp.json)
        - Name & Profiel Änderungen übernehmen (db.json)
            - Neues Profiel, neue Grenzwerte ziehen wenn ängerung (triggert 2. lesen)
    - "Aktuelle Sensorwerte" Reduzieren (ø) -> Model
    - Werte Log aus "prototyp.JSON" im Model anfügen -> Model
    - "prototyp.json" auf Server (über)schreiben
    - "Aktuelle Sensorwerte" im Model zurücksetzen
        
    
    
## Button Pressed?
        - Display Ausgabe der Aktuellen werte aus Model

## Punpe Aktivieren (funktion in Control)
    - Pumpe wird für x ms aktiviert
    
## Status Change (funk in Control)
    - LEDs Aktivieren
    - Json Lesen Server -> in Model (prototyp.json)
    - Status in "prototyp.JSON" ändern
    - änderungen "prototyp.JSON" auf Server schreiben
    
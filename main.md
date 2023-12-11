# setup
    - MVC initialisierung(JSON Data) X
    - wifi connection X
    - JSON Data from server X
    
    - (set starttime) X

# loop (60 mal die Sekunde) X


## Sensoren Intervall (alle 5-10 sekunden) X
    - Lesen der Sensoren X
    - Prüfen grenzwerte
        - Falls Kritisch -> Pumpe & Status Change
    - Schreiben werte in Model (in ZyklusArray) X
        
## Server Intervall (alle 90 Sek für demo sonst 15-30 Minuten)
    - Json Lesen Server -> in Model (prototyp.json)
        - Name & Profiel Änderungen übernehmen (db.json)
            - Neues Profiel, neue Grenzwerte ziehen wenn ängerung (triggert 2. lesen)
    - "Aktuelle Sensorwerte" Reduzieren (ø) -> Model X
    - Werte Log aus "prototyp.JSON" im Model anfügen -> Model
    - "prototyp.json" auf Server (über)schreiben
    - "Aktuelle Sensorwerte" im Model zurücksetzen X
        
    
    
## Button Pressed?
        - Display Ausgabe der Aktuellen werte aus Model

## Pumpe Aktivieren (funktion in Control)
    - Pumpe wird für x ms aktiviert
    
## Status Change (funk in Control)
    - LEDs Aktivieren
    - Json Lesen Server -> in Model (prototyp.json)
    - Status in "prototyp.JSON" ändern
    - änderungen "prototyp.JSON" auf Server schreiben
    

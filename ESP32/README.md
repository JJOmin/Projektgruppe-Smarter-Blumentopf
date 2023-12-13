# Programmablauf
## setup
    - MVC initialisierung(JSON Data) X
    - wifi connection X
    - JSON Data from server X
    
    - (set starttime) X

## loop (60 mal die Sekunde) X


### Sensoren Intervall (alle 5-10 sekunden) X
    - Lesen der Sensoren X
    - Prüfen grenzwerte X
        - Falls Kritisch -> Status Change X
    - Schreiben werte in Model (in ZyklusArray) X
        
### Server Intervall (alle 90 Sek für demo sonst 15-30 Minuten)
    - Json Lesen Server -> in Model (prototyp.json) X
        - Name & Profiel Änderungen übernehmen (db.json) X
            - Neues Profiel, neue Grenzwerte ziehen wenn ängerung (triggert 2. lesen) X
    - "Aktuelle Sensorwerte" Reduzieren (ø) -> Model X
    - Werte Log aus "prototyp.JSON" im Model anfügen -> Model X
    - "prototyp.json" auf Server (über)schreiben X
    - "Aktuelle Sensorwerte" im Model zurücksetzen X
        
    
    
### Button Pressed?
        - Display Ausgabe der Aktuellen werte aus Model X

### Pumpe Aktivieren (funktion in Control)
    - Pumpe wird für x ms aktiviert
    
### Status Change (funk in Control)
    - LEDs Aktivieren X
    - Json Lesen Server -> in Model (prototyp.json) X
    - Status in "prototyp.JSON" ändern X
    - änderungen "prototyp.JSON" auf Server schreiben X
    

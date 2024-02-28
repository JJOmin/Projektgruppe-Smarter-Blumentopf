import utime

def pumpensteuerung():
    min_feuchtigkeit = 0  # Wenn der Sensor auf min oder 0 ist 

    while True:
        feuchtigkeit = feuchtigkeit_sensor()

        if feuchtigkeit <= min_feuchtigkeit:
            pumpe_giessen() # hier die pumpe an für eine sek
            print("Pumpe sperrt für 1 Stunde...")
            time.sleep(3600)  # Pumpe sperrt für 1 Stunde (3600 Sekunden)

        print("Feuchtigkeitsmessung abgeschlossen.")

        time.sleep(50000)  # Verzögerung zwischen den Feuchtigkeitsmessungen
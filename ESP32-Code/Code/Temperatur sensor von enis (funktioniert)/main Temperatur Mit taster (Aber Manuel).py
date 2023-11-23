import machine, onewire, ds18x20, time

<<<<<<< HEAD
class Temperatur:
    def __init__(self, ds_pin, btn_pin): 
        self.ds_pin = machine.Pin(ds_pin) #Initialisierung
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin))
        self.btnYellow = machine.Pin(btn_pin, machine.Pin.IN)
        self.roms = self.ds_sensor.scan() #Suche nach DS18B20-Sensoren
        print('Found DS devices: ', self.roms) #Ausgabe der gefundenen Adressen:
        self.running = False # Maybe muss das true sein(noch nicht sicher)

    def read_temperature(self): # funktion ließ die Temperatur 
        self.ds_sensor.convert_temp()
        time.sleep_ms(750) # pause würde ich empfehlen 
        for rom in self.roms:
            temperature = self.ds_sensor.read_temp(rom)
            print("Temperatur: {:.2f}°C".format(temperature))

    def start_by_press(self): # die schleife wird so lange fortgefürt bis der taster unterbricht.
        self.running = True
        while self.running: #endloschschleife bis 
            self.read_temperature()
            if self.btnYellow.value() == 0:  # hier muss irgendwie ein fehler sein(Vermutlich)
                self.running = False
                break

# Instanzierung der Klasse
temperatur_sensor = Temperatur(ds_pin=22, btn_pin=34) #wichtig geht nur mit Pin22

while True:
    #temperatur_sensor.start_by_press()
    #time.sleep(2)
    if temperatur_sensor.btnYellow.value():
        temperatur_sensor.read_temperature()
    
    
=======

########## Beginn Klasse ##############  
class Temperatur:
    def __init__(self, ds_pin, btn_pin):
        self.ds_pin = machine.Pin(ds_pin)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin)) # Um den Sensor anzusprechen!(über ein OneWire bus system)
        self.btnYellow = machine.Pin(btn_pin, machine.Pin.IN)
        self.roms = self.ds_sensor.scan() #Scannen nach DS18B20-Geräten
        print('Found DS devices: ', self.roms) #sicherstellung ob senor richtig angeschlossne ist
        self.running = False  # Beachte: Es sollte "self.running" sein, nicht "self.runnig"

    def read_temperature(self):
        self.ds_sensor.convert_temp() # Sensor, mache bitte Messung!
        time.sleep_ms(750) # Messpuffer (empfohlen, ihn zu behalten)
        for rom in self.roms:
            temperature = self.ds_sensor.read_temp(rom)
            print("Temperatur: {:.2f}°C".format(temperature)) # Der Ausdruck im Display/konsole

    def start_by_press(self):
        self.running = True #Setzt self.runnig auf True.
        while self.running: #Solange True ist
            self.read_temperature() #führe funktion lesen der temperatur aus solange 
            if self.btnYellow.value() == 1: # Überprüfe, ob der Taster gedrückt ist
                self.running = False # Starte die Temperaturmessung
########## Ende Klasse ##############            
            
# Instanzierung der Klasse
temperatur_sensor = Temperatur(ds_pin=22, btn_pin=34)# WICHTIG hier funktioniert es nur mit Pin 22

while True:
    if temperatur_sensor.btnYellow.value() == 0: 
        temperatur_sensor.start_by_press()
    time.sleep(0.1) # Kurze Pause, um den Tasterstatus stabil zu halten
>>>>>>> 2548101b005c34b431766760680028c37728871a

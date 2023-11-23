import machine, onewire, ds18x20, time

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
    temperatur_sensor.start_by_press()
    time.sleep(2)
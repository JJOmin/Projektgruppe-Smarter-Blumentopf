import machine, onewire, ds18x20, time

from Controller import Controller

class Temperatur:
    def __init__(self, ds_pin, btn_pin): 
        self.ds_pin = machine.Pin(ds_pin) # pin für Sensor
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin)) # Kominikation mit Sensor
        self.btnYellow = machine.Pin(btn_pin, machine.Pin.IN) # Taster(hier zufällig gelb)
        self.roms = self.ds_sensor.scan() #Suche nach DS18B20-Sensoren
        print('Found DS devices: ', self.roms) #Ausgabe der gefundenen Adressen:
        self.running = False # Maybe muss das true sein(noch nicht sicher)

    def read_temperature(self): #Funktion ließ die Temperatur 
        self.ds_sensor.convert_temp() #Umwandlung (koventierung) der werte in Temperatur werte
        time.sleep_ms(750) #pause würde ich empfehlen 
        for rom in self.roms: # solange self.roms werte ließt
            temperature = self.ds_sensor.read_temp(rom) # temperatur = die gelesenen Koventierten werte
            print("Temperatur: {:.2f}°C".format(temperature)) #Ausgabe der Temperatur + Formatierung

    def start_by_press(self): # die schleife wird ausgeführt wenn der taster gedrückt wird
        self.running = True # S
        while self.running: # endloschschleife solange 
            self.read_temperature()
            if self.btnYellow.value() == 0: #
                self.running = False
                break
            
            

# Instanzierung der Klasse. Instanzierung in die Main??? 
temperatur_sensor = Temperatur(ds_pin=22, btn_pin=34) #wichtig geht nur mit Pin22

while True: # Endlosschleife die darauf wartet das Btn gedrückt wird und dann Methoden istanziert
    if temperatur_sensor.btnYellow.value(): # wenn der wert vom btn True ist
        temperatur_sensor.read_temperature() # startet diese Methode
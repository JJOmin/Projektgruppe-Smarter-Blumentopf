import machine, onewire, ds18x20, time

class TemperatureSensor:
    def __init__(self, tempData): #btn_pin
        self.ds_pin = machine.Pin(tempData['dpin']) # pin für Sensor
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin)) # Kominikation mit Sensor
        self.roms = self.ds_sensor.scan() #Suche nach DS18B20-Sensoren
        self.running = False # Maybe muss das true sein(noch nicht sicher)
    

    def readTemperature(self): #Funktion ließ die Temperatur 
        self.ds_sensor.convert_temp() #Umwandlung (koventierung) der werte in Temperatur werte
        time.sleep_ms(750) #pause würde ich empfehlen 
        for rom in self.roms: # solange self.roms werte ließt
            temperature = self.ds_sensor.read_temp(rom) # temperatur = die gelesenen Koventierten werte
            return temperature


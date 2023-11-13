import machine
import onewire
import ds18x20
import time

ds_pin = machine.Pin(22)  # WICHTIG hier funktioniert es nur mit Pin 22
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))  # Um den Sensor anzusprechen!
btnYellow = machine.Pin(34, machine.Pin.IN)  # GPIO-Pin für den gelben Taster

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

def read_temperature():
    ds_sensor.convert_temp()  # Sensor, mache bitte Messung!
    time.sleep_ms(750)  # Messpuffer (empfohlen, ihn zu behalten)
    for rom in roms:
        temperature = ds_sensor.read_temp(rom)
        print("Temperatur: {:.2f}°C".format(temperature))  # Der Ausdruck im Display

running = False

while True:
    if btnYellow.value() == 0:  # Überprüfe, ob der Taster gedrückt ist
        running = True  # Starte die Temperaturmessung
        while running:
            read_temperature()
            if btnYellow.value() == 1:  # Überprüfe, ob der Taster losgelassen wurde
                running = False  # Beende die Temperaturmessung, wenn der Taster losgelassen wird
    time.sleep(0.1)  # Kurze Pause, um den Tasterstatus stabil zu halten

import machine, onewire, ds18x20, time #Module und Bibliotheken
 
ds_pin = machine.Pin(22) 								# WICHTIG hier funktioniert es nur mit Pin22
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin)) 	# Um den Sensor anzusprechen!
 
roms = ds_sensor.scan()
print('Found DS devices: ', roms)
 
while True:
  ds_sensor.convert_temp() 			# Sensor mach bitte Messung!
  time.sleep_ms(750) 				#Messpuffer (empfohlen bei zu behalten)
  for rom in roms:
    print("Temperatur: {",ds_sensor.read_temp(rom),"°}") 	# Der print im display
  time.sleep(5) 													#Gibt den wert alle 5sek aus
#main
#from Server import Server
from Control import Control
from TemperatureSensor import TemperatureSensor

control = Control()
#control.serverTest() #Tests the server Connection (on the Hotspot of Leos Phone)
#control.sensorSoilTest() #funktioniert

#while True: # Endlosschleife die darauf wartet das Btn gedrückt wird und dann Methoden istanziert
    #if temperatur_sensor.btnColor.value(): # wenn der wert vom btn True ist
     #   temperatur_sensor.read_temperature() # Startet diese Methode


#Für Enis zum Testen
#control.sensorTemperatureTest() #Tests the Temp Sensor, on Pin 22
#control.sensorTemperatureTest()
#tempData = {'dpin': 22}  # Beispiel-Pin, ersetze dies durch den tatsächlichen Pin
#temperature_sensor_instance = TemperatureSensor(tempData)

#Für Sam zum Testen
#control.sensorLightTest() #Tests the LightSensor on Pins {'scl':22, 'sda': 21}
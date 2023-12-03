#main
from Control import Control


control = Control()
hile True:
    control.startByPress()
    #control.serverTest()#Tests the server Connection (on the Hotspot of Leos Phone)

    #control.sensorSoilTest() #funktioniert
    
    if control.model.btnData == 0:  # Annahme: btnData ist ein Integer-Wert
        control.sensorTemperatureTest()
        control.sensorLightTest()

#Für Enis zum Testen
 #Tests the Temp Sensor, on Pin 22
#temperature_sensor_instance = TemperatureSensor(tempData)

#Für Sam zum Testen
 #Tests the LightSensor on Pins {'scl':22, 'sda': 21}
#main
from Control import Control

control = Control()

while True:
    control.startByPress()
    #print(control.btnColor.value())
    #control.serverTest()
    #control.sensorSoilTest()
    #control.serverTest()#Tests the server Connection (on the Hotspot of Leos Phone)

    
    if control.model.btnData == 0:  # Annahme: btnData ist ein Integer-Wert
        control.sensorTemperatureTest() # funktioniert
        control.sensorSoilTest()
        control.sensorLightTest()
         


#Für Sam zum Testen
 #Tests the LightSensor on Pins {'scl':22, 'sda': 21}
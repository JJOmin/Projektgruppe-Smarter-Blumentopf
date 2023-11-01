import machine
import onewire
import ds18x20
import utime

#Variable definition
ds18DataPin = machine.Pin(36)  # Pin 36 verbunden mit DQ pin des DS18B20 Sensors
ds18Sensor = ds18x20.DS18X20(onewire.OneWire(ds18DataPin))


# Function
def getTempSensor():
        try:
            sensorScan = ds18Sensor.scan()
            ds18Sensor.convert_temp()
            utime.sleep_ms(750)  # Wartet 750ms auf "ds18Sensor.convert_temp()" (750ms for 12-bit resolution)
            for i in sensorScan:
                tempRaw = ds18Sensor.read_temp(i)
            return tempRaw

        except Exception as e:
            return "Error: {}".format(e)



# Execution of function
while True:
    tempNow = getTempSensor()
    tempNowFormated = "{:.2f}°C".format(tempNow) #Formatierung von float in String
    print("TempRaw: "+ str(tempNow)) #Ausgabe der unformatierten Messung (nicht gerundet)
    print("TempFormated: "+ tempNowFormated) #Ausgabe der formatierten Messung in °C (gerundet)
    print()

    utime.sleep(3)  # Wartet 3 Sekunden bis zu neuen Messung


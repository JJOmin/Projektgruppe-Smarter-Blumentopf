import machine
import onewire
import ds18x20
import utime

#Variable definition
ds18DataPin = machine.Pin(36)  # Pin 36 is connected to the DQ pin of DS18B20 sensor
ds18Sensor = ds18x20.DS18X20(onewire.OneWire(ds18DataPin))
repetition = 0

# Function
def tempSensorTest():
    while True:
        try:
            sensorScan = ds18Sensor.scan()
            ds18Sensor.convert_temp()
            utime.sleep_ms(750)  # Wait for the temperature conversion to complete (750ms for 12-bit resolution)
            
            for i in sensorScan:
                temperature = ds18Sensor.read_temp(i)
                print("Temperature: {:.2f}°C".format(temperature))
                repetition +=1
                
            utime.sleep(3)  # Wait for 3 seconds before the next temperature reading
        except Exception as e:
            print("Error: {}".format(e))



# Execution of function
tempSensorTest()


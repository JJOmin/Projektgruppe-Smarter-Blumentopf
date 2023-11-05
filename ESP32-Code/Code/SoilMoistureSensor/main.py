# Import necessary libraries
from machine import Pin, ADC
import machine
import utime


# GPIO pins used:
pinSoilMoisture = 35  # pin for Soil Moisture Sensor
led_pin = machine.Pin(26, machine.Pin.OUT)
button_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)  # PULL_UP activates the internal Pull-Up resistor

adc = ADC(Pin(pinSoilMoisture))  # Initialize ADC (Analog to Digital Converter) on the sensor pin

# Constants for The calculation


percentageArray = []
rawValueArray = []
durchschnitt = 0
dry = 4095
wet = 0

last_moisture_read_time = 0
kalibrationLoops = 0

# Heartbeat-Funktion mit Button-Erkennung
def button(led_pin, button_pin):
    # Wenn der Button gedrückt wird (niedriger Pegel), schalte die LED ein
    if button_pin.value() != 1:
        led_pin.on()
    else:
        led_pin.off()

def map_range(value, from_min, from_max, to_max, to_min):
    # Translates a range of numbers into another range of numbers
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled_value = (value - from_min) / from_range
    mapped_value = to_min + (scaled_value * to_range)
    return mapped_value

def moistureSensor(adc, dry, wet):
    global last_moisture_read_time
    current_time = utime.ticks_ms()
    # Read analog value from the sensor every 10 seconds
    if current_time - last_moisture_read_time >= 1000:  # 10 seconds in milliseconds
        sensor_value = adc.read()
        moisture_percentage = map_range(sensor_value, wet, dry, 0, 100)
        #print(moisture_percentage, dry, wet, sensor_value)
        print("Moisture Percentage: {:.2f}%".format(moisture_percentage),"  Raw Sensor Data:",sensor_value)
        last_moisture_read_time = current_time
        
        #print(map_range(3700, 3700, 4095, 0, 100))
        
        #print(map_range(4095, 3700, 4095, 0, 100))
        
        
def moistureSensorKalibration(numKalibrationValues, adc):
    global last_moisture_read_time
    global kalibrationLoops
    global wet
    global dry
    current_time = utime.ticks_ms()
    


    if kalibrationLoops < numKalibrationValues:
        if current_time - last_moisture_read_time >= 1000:  # 1 second in milliseconds
            sensor_value = adc.read()
            rawValueArray.append(sensor_value)
            kalibrationLoops += 1
            #print("Raw: [Avg, Min, Max, Diff, numValues]")
            #print([average(rawValueArray),min(rawValueArray),max(rawValueArray),max(rawValueArray) - min(rawValueArray), kalibrationLoops])
            print("Kalibration Running for",kalibrationLoops, "Seconds and",numKalibrationValues - kalibrationLoops,"Seconds left.")
            last_moisture_read_time = current_time
    elif kalibrationLoops == numKalibrationValues:
        wetMin = min(rawValueArray)
        wetMax = max(rawValueArray)
        wet = max(rawValueArray)
        #dry = max(rawValueArray)
        print("")
        print("Kalibration is over")
        print("Wet Average Value: ",average(rawValueArray))
        print("Min Wet Value:",wetMin)
        print("Max Wet Value:",wetMax)
        print("Dry Value:",dry)
        print("Wet Value:",wet)
        print("Maximum Wet Differenz: ",max(rawValueArray) - min(rawValueArray))
        print("")
        
        kalibrationLoops += 1
        
    else:
    
        moistureSensor(adc,dry,wet)
            
        
    
    
        
#-----------------------Math Stuff-----------------------#
def average(array):
    sumArray = sum(array)
    numElements = len(array)
    return sumArray / numElements
#--------------------------------------------------------#

#--------------------------Main--------------------------#
def main(adc, led_pin, button_pin):
    while True:
        #moistureSensor(adc)
        moistureSensorKalibration(100, adc)
        button(led_pin, button_pin)
        
#--------------------------------------------------------#

main(adc, led_pin, button_pin)

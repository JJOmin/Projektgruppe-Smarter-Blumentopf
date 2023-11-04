# Import necessary libraries
from machine import Pin, ADC
import time
import machine


#GPIO pins used:
pinSoilMoisture = 35 #pin for Soil Moisture Sensor
led_pin = machine.Pin(26, machine.Pin.OUT)
button_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)  # PULL_UP aktiviert den internen Pull-Up Widerstand

adc = ADC(Pin(pinSoilMoisture)) # Initialize ADC (Analog to Digital Converter) on the sensor pin

#Constants for The calculation
dry = 4095
wet = 2000


# Heartbeat-Funktion mit Button-Erkennung
def button(led_pin, button_pin):
   
    # Wenn der Button gedrückt wird (niedriger Pegel), schalte die LED ein
    if button_pin.value() != 1:
        led_pin.on()
            
    else:
        led_pin.off()

def map_range(value, from_min, from_max, to_min, to_max):
    #Translates a range of numbers into another range of numbers
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled_value = (value - from_min) / from_range
    mapped_value = to_min + (scaled_value * to_range)
    return mapped_value


def moistureSensor(adc,i):
    
    if i > 300:
        print("Hier")
        # Read analog value from the sensor
        sensor_value = adc.read()
        print("Sensor values Raw:",sensor_value)
        # Convert analog value to percentage (assuming 0 as dry and 4095 as wet)
        #moisture_percentage = ((4095 - sensor_value) / 4095)* 100

        # Print the moisture percentag
        print("Moisture Percentage: {:.2f}%".format(map_range(sensor_value, wet,dry,100,0)))

        #time.sleep(10) #waiting 10 seconds
        i = 0
        return i
    else
        i = i+1
        return i
   


i = 0
def main(adc, led_pin, button_pin):
    i = moistureSensor(adc, i)
    button(led_pin, button_pin)
    

 main(adc, led_pin, button_pin)

    









# Import necessary libraries
from machine import Pin, ADC
import time

# Define the GPIO pin to which the sensor is connected
sensor_pin = 32 # Change this to the GPIO pin you've connected the sensor to

# Initialize ADC (Analog to Digital Converter) on the sensor pin
adc = ADC(Pin(sensor_pin))

while True:
    # Read analog value from the sensor
    sensor_value = adc.read()
    print("Sensor values Raw:",sensor_value)
    # Convert analog value to percentage (assuming 0 as dry and 4095 as wet)
    moisture_percentage = ((4095 - sensor_value) / 4095)* 100

    # Print the moisture percentage
    print("Moisture Percentage: {:.2f}%".format(moisture_percentage))
    if moisture_percentage < 1:
        print("Etwas Trocken hier")

    # Wait for some time before reading again (e.g., 1 second)
    time.sleep(10)

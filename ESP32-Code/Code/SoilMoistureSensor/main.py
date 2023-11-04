# Import necessary libraries
from machine import Pin, ADC
import time
import machine


# Definiere die Pins für die LED (hier: Pin 2) und den Button (hier: Pin 4)
led_pin = machine.Pin(26, machine.Pin.OUT)
button_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)  # PULL_UP aktiviert den internen Pull-Up Widerstand
sensor_pin = 35 # Change this to the GPIO pin you've connected the sensor to
# Initialize ADC (Analog to Digital Converter) on the sensor pin
adc = ADC(Pin(sensor_pin))
#led_pin.off()

# Heartbeat-Funktion mit Button-Erkennung
def button(led_pin, button_pin):
    while True:
        # Wenn der Button gedrückt wird (niedriger Pegel), schalte die LED ein
        if not button_pin.value():
            led_pin.on()
            
        else:
            led_pin.off()

# Rufe die Heartbeat-Funktion mit Button-Erkennung auf


while True:
    # Read analog value from the sensor
    sensor_value = adc.read()
    #print("Sensor values Raw:",sensor_value)
    # Convert analog value to percentage (assuming 0 as dry and 4095 as wet)
    moisture_percentage = ((4095 - sensor_value) / 4095)* 100

    # Print the moisture percentage
    print("Moisture Percentage: {:.2f}%".format(moisture_percentage), "Raw Values:",sensor_value)
        
    # Wait for some time before reading again (e.g., 1 second)
    time.sleep(10)

button(led_pin, button_pin)

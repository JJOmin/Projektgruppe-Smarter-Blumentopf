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
dry = 4095
wet = 2000

last_moisture_read_time = 0

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

def moistureSensor(adc):
    global last_moisture_read_time
    current_time = utime.ticks_ms()
    # Read analog value from the sensor every 10 seconds
    if current_time - last_moisture_read_time >= 10000:  # 10 seconds in milliseconds
        sensor_value = adc.read()
        moisture_percentage = map_range(sensor_value, wet, dry, 0, 100)
        print("Moisture Percentage: {:.2f}%".format(moisture_percentage),"   Raw Sensor Data:",sensor_value)
        last_moisture_read_time = current_time

def main(adc, led_pin, button_pin):
    while True:
        moistureSensor(adc)
        button(led_pin, button_pin)

main(adc, led_pin, button_pin)

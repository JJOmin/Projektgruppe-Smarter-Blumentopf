import machine
import math, time
from machine import SoftI2C, Pin
#from Controller import Controller


class LichtSensor:
    def __init__(self, scl_pin, sda_pin):
        self.scl_pin = machine.Pin(scl_pin)
        self.sda_pin = machine.Pin(sda_pin)
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        
        
    def read_values(self):# Convert raw data to make it readible for esp
        data = self.sda_pin.readfrom(0x23, 2)
        light_level = (data[0] << 8 | data[1]) / 1.2 #data vom sensor
        #time.sleep_ms(1000)
        return light_level
    
        
        
    def auslesen(self):
        analog_value = self.read_values
        voltage = analog_value / 1024 * 5
        resistance = 2000.0 * voltage / (1 - voltage / 5)
        lux = (50.0 * 1e3 * pow(10.0, 0.7) / resistance) ** (1.0 / 0.7) #standard umrechnung lt 

        print(analog_value, lux)

        if math.isfinite(lux):
            print("The brightness is {:.2f} lx".format(lux))
        else:
            print("Too bright to measure")

        time.sleep_ms(1000)
        
scl= Pin(22, Pin.OUT)
sda= Pin(21, Pin.OUT)
sensor = LichtSensor(scl, sda)
    
while True:
    sensor.auslesen()
        #
import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

class Display:
    def __init__(self):
        self.I2C_ADDR = 0x27
        self.totalRows = 2
        self.totalColumns = 16

        try:
            self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # I2C für ESP32
            # i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)  # I2C für ESP8266
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.totalRows, self.totalColumns)
        except Exception as e:
            print("Fehler beim Initialisieren des LCDs:", e)

    def displayausgabe(self, text):
        try:
            self.lcd.clear()
            self.lcd.putstr(str(text))
            sleep(1)
        except Exception as e:
            print("Fehler beim Schreiben auf das LCD:", e)



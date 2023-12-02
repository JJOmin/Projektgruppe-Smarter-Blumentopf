import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import utime


class Display:
    def __init__(self):
        self.I2C_ADDR = 0x27
        self.totalRows = 2
        self.totalColumns = 16
        self.last_measure_time = 0

        try:
            self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # I2C für ESP32
            # i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)  # I2C für ESP8266
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.totalRows, self.totalColumns)
        except Exception as e:
            print("Fehler beim Initialisieren des LCDs:", e)

    def displayausgabe(self, text, delay_ms=2000):
        try:
            # Clear the LCD once before displaying any text
            self.lcd.clear()

            # Zeichen pro Zeile
            chars_per_line = self.totalColumns * self.totalRows

            # Text in Teile aufteilen
            text_parts = [text[i:i + chars_per_line] for i in range(0, len(text), chars_per_line)]
            current_time = utime.ticks_ms()

            for part in text_parts:
                self.lcd.clear()
                if current_time - self.last_measure_time >= delay_ms:
                    # Only update the content without clearing the LCD
                    self.lcd.move_to(0, 0)  # Move the cursor to the beginning
                    self.lcd.putstr(part)
                    self.last_measure_time = current_time

                    # Pausiere für die angegebene Zeit in Millisekunden
                    utime.sleep_ms(delay_ms)
                    current_time = utime.ticks_ms()  # Aktualisiere die aktuelle Zeit

        except Exception as e:
            print("Fehler beim Schreiben auf das LCD:", e)




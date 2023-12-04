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
        self.current_display_text = ""  # Add this line

        try:
            self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # I2C für ESP32
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.totalRows, self.totalColumns)
        except Exception as e:
            print("Fehler beim Initialisieren des LCDs:", e)

    def displayausgabe(self, text, delay_ms=3000):
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
                    # Nur update die Inhalte, ohne das gesamte LCD zu löschen
                    self.lcd.move_to(0, 0)  # Cursor an den Anfang setzen
                    self.lcd.putstr(part)
                    self.last_measure_time = current_time

                    # Warte für die angegebene Zeit in Millisekunden
                    wait_until = current_time + delay_ms
                    
                    while utime.ticks_ms() < wait_until:
                        pass  # Warte, ohne den gesamten ESP zu blockieren
                    current_time = utime.ticks_ms()  # Aktualisiere die aktuelle Zeit
               
                   

        except Exception as e:
            print("Fehler beim Schreiben auf das LCD:", e)


    def display_centered_text(self, text, delay_ms=2000):
        try:
            self.lcd.clear()

            chars_per_line = self.totalColumns
            parts = text.split(':')
            lines = []

            for i in range(0, len(parts), 2):
                key = parts[i].strip()
                value = parts[i + 1].strip() if i + 1 < len(parts) else ""
                lines.append(key)
                lines.append(value)

            centered_lines = [(chars_per_line - len(line)) // 2 * ' ' + line + ' ' * ((chars_per_line - len(line)) // 2) for line in lines]

            self.lcd.clear()

            current_time = utime.ticks_ms()
            idx = 0

            while idx < len(centered_lines):
                if utime.ticks_ms() - current_time >= delay_ms:
                    if idx % 2 == 0:
                        self.lcd.clear()
                    self.lcd.putstr(centered_lines[idx])
                    idx = (idx + 1) % len(centered_lines)
                    current_time = utime.ticks_ms()
                    print(idx)
                    if idx == 0:
                        break

        except Exception as e:
            print("Fehler beim Schreiben auf das LCD:", e)


    def update_display_text(self, new_text):
        self.current_display_text = new_text

    def display_updated_text(self):
        self.display_centered_text(self.current_display_text)

# Beispielaufruf
#display = Display()
#x = 0
#current_time = utime.ticks_ms()

#while True:
    #print(x)
    #display_text = "Feuchtigkeit:" + str(x) + "%:Temperatur:" + str(x) + ":Licht:" + str(x)+":"
    #display.update_display_text(display_text)
    #display.display_updated_text()
    #x += 1      
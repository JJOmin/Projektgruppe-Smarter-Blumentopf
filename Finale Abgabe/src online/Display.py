import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import utime


class Display:
    def __init__(self):
        self.I2C_ADDR = 0x27
        self.totalRows = 2
        self.totalColumns = 16
        self.current_display_text = ""  # Hinzufügen dieser Zeile zur Initialisierung
        self.grad = bytearray([0x07,0x05,0x07,0x00,0x00,0x00,0x00,0x00])
        

        try:
            # Initialisiere den I2C-Bus und das LCD
            self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # I2C für ESP32
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.totalRows, self.totalColumns)
            self.lcd.custom_char(0, self.grad)
            self.lcd.display_off()
            self.lcd.backlight_off()
        except Exception as e:
            # Fehlerausgabe, falls die Initialisierung fehlschlägt
            print("Fehler beim Initialisieren des LCDs:", e)

            
    def displayausgabe(self, text, delay_ms=3000):
        try:
            # LCD einmal löschen, bevor irgendein Text angezeigt wird
            self.lcd.clear()

            # Zeichen pro Zeile
            chars_per_line = self.totalColumns * self.totalRows

            # Text in Teile aufteilen
            text_parts = [text[i:i + chars_per_line] for i in range(0, len(text), chars_per_line)]
            current_time = utime.ticks_ms()

            for part in text_parts:
                self.lcd.clear()
                if current_time - self.last_measure_time >= delay_ms:
                    # Nur die Inhalte aktualisieren, ohne das gesamte LCD zu löschen
                    self.lcd.move_to(0, 0)  # Cursor an den Anfang setzen
                    self.lcd.putstr(part)
                    self.last_measure_time = current_time

                    # Warte für die angegebene Zeit in Millisekunden
                    wait_until = current_time + delay_ms

                    # Warte, ohne den gesamten ESP zu blockieren
                    while utime.ticks_ms() < wait_until:
                        pass
                    current_time = utime.ticks_ms()  # Aktualisiere die aktuelle Zeit

        except Exception as e:
            print("Fehler beim Schreiben auf das LCD:", e)

                
    def display_centered_text(self, text, delay_ms=2000):
        try:
            # LCD zu Beginn löschen
            self.lcd.clear()

            # Zeichen pro Zeile auf dem Display
            chars_per_line = self.totalColumns

            # Text in Teile (Schlüssel-Wert-Paare) aufteilen
            parts = text.split(':')
            lines = []

            # Schlüssel-Wert-Paare erstellen
            for i in range(0, len(parts), 2):
                key = parts[i].strip()
                value = parts[i + 1].strip() if i + 1 < len(parts) else ""
                lines.append(key)
                lines.append(value)

            # Jede Zeile zentrieren und Leerzeichen für die Ausrichtung hinzufügen
            centered_lines = [
                (chars_per_line - len(line)) // 2 * ' ' + line + ' ' * ((chars_per_line - len(line)) // 2)
                for line in lines
            ]

            # LCD zu Beginn löschen
            self.lcd.clear()

            # Aktuelle Zeit für die Zeitmessung
            current_time = utime.ticks_ms()
            idx = 0

            # Schleife für die Anzeige des zentrierten Texts
            while idx < len(centered_lines):
                # Überprüfen, ob genügend Zeit seit dem letzten Update vergangen ist
                if utime.ticks_ms() - current_time >= delay_ms:
                    
                    # LCD löschen, wenn eine neue Schlüsselzeile beginnt
                    if idx % 2 == 0:
                        self.lcd.clear()
                    
                    # Überprüfen, ob die Schlüsselzeile zu lang für eine Zeile ist
                    if len(lines[idx]) >= 16:
                        # Scrollen der Schlüsselzeile, wenn sie zu lang ist
                        if idx % 2 == 0:
                            # Wenn es noch eine Wertzeile gibt, diese anzeigen
                            if len(centered_lines) > idx + 2:
                                self.lcd.move_to(0, 1)
                                self.lcd.putstr(centered_lines[idx + 1])
                            self.lcd.move_to(0, 0)
                            self.scroll_text(lines[idx], 100)
                            idx = (idx + 1) % len(centered_lines)
                        # Fortsetzen mit der nächsten Zeile im Falle einer Wertzeile
                        else:
                            idx = (idx + 1) % len(centered_lines)
                    else:
                        # Anzeigen der aktuellen Zeile
                        self.lcd.putstr(centered_lines[idx])
                        idx = (idx + 1) % len(centered_lines)
                    
                    # Aktuelle Zeit für die nächste Zeitmessung aktualisieren
                    current_time = utime.ticks_ms()

                    # Wenn wieder die erste Zeile (Schlüsselzeile) erreicht wurde, die Schleife beenden
                    if idx == 0:
                        break

        except Exception as e:
            # Fehlermeldung ausgeben, falls ein Fehler auftritt
            print("Fehler beim Schreiben auf das LCD(centern):", e)



    def update_display_text(self, new_text):
       
        self.current_display_text = new_text
        

    def display_updated_text(self):
        self.lcd.display_on()
        self.lcd.backlight_on()
        self.display_centered_text(self.current_display_text)
        self.lcd.display_off()
        self.lcd.backlight_off()
        

    def scroll_text(self, text, scroll_speed=100):
        try:
            text_length = len(text)
            # Den Text für ein reibungsloses Scrollen duplizieren und ein Leerzeichen dazwischen fügen
            display_text = text + " " + text
            # Die Schleife umfasst den gesamten Text plus zwei Zeichen (eine Leerzeichenlücke am Ende)
            for i in range(text_length + 2):
                # Cursor auf den Anfang des LCD setzen
                self.lcd.move_to(0, 0)
                # Nur einen Ausschnitt des duplizierten Texts anzeigen, um zu scrollen
                self.lcd.putstr(display_text[i:i + self.totalColumns])
                
                # Ihre eigene Timing-Logik hier implementieren (ohne sleep)
                start_time = utime.ticks_ms()
             
        except Exception as e:
            # Fehlermeldung ausgeben, falls ein Fehler auftritt
            print("Fehler beim Schreiben auf das LCD(Scrollen):", e)
    


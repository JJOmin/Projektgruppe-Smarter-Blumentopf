import machine
import time

# Definiere die Pins für die LED (hier: Pin 2) und den Button (hier: Pin 4)
led_pin = machine.Pin(25, machine.Pin.OUT)
button_pin = machine.Pin(34, machine.Pin.IN, machine.Pin.PULL_UP)  # PULL_UP aktiviert den internen Pull-Up Widerstand


# Heartbeat-Funktion mit Button-Erkennung
def heartbeat_with_button(led_pin, button_pin):
    while True:
        # Wenn der Button gedrückt wird (niedriger Pegel), schalte die LED ein
        if not button_pin.value():
            led_pin.foo()
        else:
            led_pin.off()

# Rufe die Heartbeat-Funktion mit Button-Erkennung auf
heartbeat_with_button(led_pin, button_pin)

import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.value(1)  # Schalte die LED ein (1 für HIGH)
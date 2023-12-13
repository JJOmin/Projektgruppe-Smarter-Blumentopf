### Model

self.ledPins = {"light": 10, "moisture": 11, "temperature": 12}

self.stats = {"light": "Okay", "moisture": "Warning", "temperature": }

### Control

self.leds = {
    "light": machine.Pin(self.model.ledPins["light"], Pin.OUT),
    "temperature": machine.Pin(self.model.ledPins["temperature"], Pin.OUT),
    "moisture": machine.Pin(self.model.ledPins["moisture"], Pin.OUT)
    }

def statusChange(self):
    updateLeds(self.model.status)
    
def updateLeds(stats):
    for key, value in stats.items():
        if value == "Okay":
            self.leds[key].on()
        elif value == "Warning":
            self.leds[key].off()
        
    

### Main

### View
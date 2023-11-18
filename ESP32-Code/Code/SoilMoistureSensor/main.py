# Import necessary libraries
from machine import Pin, ADC
import machine
import utime
from machine import Pin, SoftI2C # fürs Display
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27     # fürs Display
totalRows = 2
totalColumns = 16


try:
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  
   
    lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
except Exception as e:
    print("Fehler beim Initialisieren des LCDs:", e)


# GPIO pins used:
pinSoilMoisture = 35  # pin for Soil Moisture Sensor
led_pin = machine.Pin(26, machine.Pin.OUT) #Pin for the LED
button_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)  # PULL_UP activates the internal Pull-Up resistor


#-----------------------Globals-----------------------#
adc = ADC(Pin(pinSoilMoisture))  # Initialize ADC (Analog to Digital Converter) on the sensor pin
percentageArray = []
rawValueArray = []
durchschnitt = 0
dry = 4095
wet = 0
last_moisture_read_time = 0
kalibrationLoops = 0

#---------------------------------------------------#


#-----------------------Functions-----------------------#
def displayausgabe(text):
    
    try:
        lcd.clear()
        lcd.putstr(str(text))
        sleep(1)
           
        
        
    except Exception as e:
        print("Fehler beim Schreiben auf das LCD:", e)



##Button der mittels Software die LED ansteuert, um Überprüfen zu können ob der ESP32 noch Läuft
def button(led_pin, button_pin):
    # Wenn der Button gedrückt wird (niedriger Pegel), schalte die LED ein
    if button_pin.value() != 1:
        led_pin.on()
    else:
        led_pin.off()
        
##Funktion die die Gemessenen werte des Soil Sensors in Prozente umrechnet
def map_range(value, from_min, from_max, to_max, to_min):
    # Überprüfen, ob from_range null ist, um eine Division durch Null zu vermeiden
    if from_max - from_min == 0:
        return 0
    
    # Translates a range of numbers into another range of numbers
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled_value = (value - from_min) / from_range
    mapped_value = to_min + (scaled_value * to_range)
    return mapped_value


##Funktion die Auf basis der angeggebenen Parameter den Soil Sensor ausliest und einen Durchschnittswert(momentanter von meist 10) wiedergibt
def moistureSensor(adc, dry, wet, numValuesAveraged, measureDuration):
    global last_moisture_read_time
    current_time = utime.ticks_ms()
    # Read analog value from the sensor every 10 seconds
    if current_time - last_moisture_read_time >= measureDuration:  # 10 seconds in milliseconds
        for i in range(0,numValuesAveraged):
            sensor_value = adc.read()
            moisture_percentage = map_range(sensor_value, wet, dry, 0, 100)
            percentageArray.append(moisture_percentage)
            rawValueArray.append(sensor_value)
            last_moisture_read_time = current_time
        
        print("Avg of",numValuesAveraged,"Measurments: Percentage: {:.2f}%".format(average(percentageArray))," Raw Sensor Data:",average(rawValueArray))
        displayausgabe("Bodenfeuchtigkeit: {:.2f}%".format(average(percentageArray)))
        print("")
    
        #Clears the list
        percentageArray.clear()
        rawValueArray.clear()
        last_moisture_read_time = current_time


##Macht ein rechtecjk um Text
def print_rechteck(text):
    print('*' * (len(text) + 4))  # Oberer Rand des Rechtecks
    print('* ' + text + ' *')      # Text mit seitlichem Rand
    print('*' * (len(text) + 4))  # Unterer Rand des Rechtecks
    
    
##Function that is used to calibrate Soil Moisture Sensores and define the Wet Value
def moistureSensorKalibration(numKalibrationValues, adc, numValuesAveraged, measureDuration):
    global last_moisture_read_time
    global kalibrationLoops
    global wet
    global dry
    current_time = utime.ticks_ms()
    
    if 0 < kalibrationLoops < numKalibrationValues:
        if current_time - last_moisture_read_time >= 1000:  # 1 second in milliseconds
            sensor_value = adc.read()
            rawValueArray.append(sensor_value)
            kalibrationLoops += 1
            print("Kalibration Running! ",numKalibrationValues - kalibrationLoops,"Values left.")
            last_moisture_read_time = current_time
            
    elif kalibrationLoops == 0:
        print_rechteck("Achtung die für die Kalibrierung muss der Sensor direkt ins Wasser gestellt werden!!!")
        kalibrationLoops += 1
            
    elif kalibrationLoops == numKalibrationValues:
        wetMin = min(rawValueArray)
        wetMax = max(rawValueArray)
        wet = max(rawValueArray)
        print("")
        print("Kalibration is over")
        print("Wet Average Value: ",average(rawValueArray))
        print("Min Wet Value:",wetMin)
        print("Max Wet Value:",wetMax)
        print("Dry Value:",dry)
        print("Wet Value:",wet)
        print("Maximum Wet to Dry Differenz: ",max(rawValueArray) - min(rawValueArray))
        print("")
        percentageArray.clear()
        rawValueArray.clear()
        
        kalibrationLoops += 1
        
    else:
        if wet > 4000:
            print("")
            print("Fehler, wert führ Wet ist zu hoch, Rekalibrierung notwendig")
            print("")
            print("Automatische Rekalibrierung Startet")
            print("")
            kalibrationLoops = 1
            
        if wet < 4000:
            moistureSensor(adc,dry,wet, numValuesAveraged, measureDuration)
        
        
#-------------------------------------------------------#
            
        

#-----------------------Math Stuff-----------------------#
def average(array):
    sumArray = sum(array)
    numElements = len(array)
    return sumArray / numElements
#--------------------------------------------------------#

#--------------------------Main--------------------------#
def main(adc, led_pin, button_pin):
    while True:
        moistureSensorKalibration(50, adc, 10, 1000) #Number of Values for Kalibration, Analog to Digital Converter, Number of Measurments for one Average Measurment, Duration of the Number of Measurments in ms
        button(led_pin, button_pin)
        
#--------------------------------------------------------#

main(adc, led_pin, button_pin)

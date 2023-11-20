from machine import Pin, ADC
import machine
import utime
from SoilMoistureSensor import SoilMoistureSensor

def button(led_pin, button_pin):
    if button_pin.value() != 1:
        led_pin.on()
    else:
        led_pin.off()

def main():
    pin_soil_moisture = 35
    dry = 4095
    wet = 0
    num_values_averaged = 10
    measure_duration = 5000  # 10 seconds in milliseconds
    numberOfCalibrationValues = 10
    numberOfCalibrations = 4
    
    led_pin = machine.Pin(26, machine.Pin.OUT)
    button_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)
    soil_sensor = Bodenfeuchtigkeitsensor(pin_soil_moisture, dry, wet, num_values_averaged, measure_duration, numberOfCalibrationValues)
    
    calibrated = 0
    
    
    while True:
        if calibrated == 0:
            soil_sensor.calibration(numberOfCalibrations)
            if soil_sensor.calibrated == True:
                calibrated = 1
        elif calibrated == 1:
            avg_moisture, avg_sensor_value = soil_sensor.read_moisture()
            if avg_moisture is not None:
                print("Avg of", num_values_averaged, "Measurements: Percentage: {:.2f}%".format(avg_moisture), " Raw Sensor Data:", avg_sensor_value)
        button(led_pin, button_pin)

if __name__ == "__main__":
    main()

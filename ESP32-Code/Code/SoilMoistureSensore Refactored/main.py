from machine import Pin, ADC
import machine
import utime

class SoilMoistureSensor:
    def __init__(self, pin, dry, wet, num_values_averaged, measure_duration, numberOfCalibrationValues):
        self.adc = ADC(Pin(pin))
        self.dry = dry
        self.wet = wet
        self.num_values_averaged = num_values_averaged
        self.measure_duration = measure_duration  # milliseconds
        self.sensor_values = []
        self.moisture_percentage = []
        self.last_measure_time = 0
        self.kalibration_loops = 0
        self.numberOfCalibrationValues = numberOfCalibrationValues
        self.calibrated = False

    def map_range(self, value, from_min, from_max, to_max, to_min):
        from_range = from_max - from_min
        to_range = to_max - to_min
        scaled_value = (value - from_min) / from_range
        mapped_value = to_min + (scaled_value * to_range)
        return mapped_value
    
    def calibration(self, num_calibration_values):
        current_time = utime.ticks_ms()

        if 0 < self.kalibration_loops < num_calibration_values:
            if current_time - self.last_measure_time >= 1000:  # 1 second in milliseconds
                sensor_value = self.adc.read()
                self.sensor_values.append(sensor_value)
                self.kalibration_loops += 1
                print("Calibration Running! {} Values left.".format(num_calibration_values - self.kalibration_loops))
                self.last_measure_time = current_time

        elif self.kalibration_loops == 0:
            print("Attention, the sensor must be placed directly into water for calibration!")
            self.kalibration_loops += 1

        elif self.kalibration_loops == num_calibration_values:
            wet_min = min(self.sensor_values)
            wet_max = max(self.sensor_values)
            self.wet = sum(self.sensor_values)/len(self.sensor_values)
            print("")
            print("Calibration is over")
            print("Wet Average Value: {:.2f}".format(sum(self.sensor_values)/len(self.sensor_values)))
            print("Min Wet Value: {}".format(wet_min))
            print("Max Wet Value: {}".format(wet_max))
            print("Dry Value: {}".format(self.dry))
            print("Wet Value: {}".format(self.wet))
            print("Maximum Wet to Dry Difference: {}".format(max(self.sensor_values) - min(self.sensor_values)))
            print("")
            self.sensor_values.clear()
            self.kalibration_loops += 1

        else:
            if self.wet > 4016:
                print("")
                print("Error, wet value is too high, recalibration required")
                print("")
                print("Automatic Recalibration Started")
                print("")
                self.calibrated = False
                self.kalibration_loops = 1

            if self.wet < 4000:
                self.calibrated = True
                
                

    def read_moisture(self):
        current_time = utime.ticks_ms()
        if current_time - self.last_measure_time >= self.measure_duration:
            for _ in range(self.num_values_averaged):
                sensor_value = self.adc.read()
                self.moisture_percentage.append(self.map_range(sensor_value, self.wet, self.dry, 0, 100))
                self.sensor_values.append(sensor_value)
            avg_percentage = sum( self.moisture_percentage) / len( self.moisture_percentage)
            avg_sensor_value = sum(self.sensor_values) / len(self.sensor_values)
            self.sensor_values.clear()
            self.moisture_percentage.clear()
            self.last_measure_time = current_time
            return avg_percentage, avg_sensor_value
        return None, None

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
    soil_sensor = SoilMoistureSensor(pin_soil_moisture, dry, wet, num_values_averaged, measure_duration, numberOfCalibrationValues)
    
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

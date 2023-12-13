from machine import Pin, ADC
import machine
import utime



class SoilSensor:
    def __init__(self, soilData): #, pin, dry, wet, numValuesAvg, measureDuration, numCalibrations
        self.adc = ADC(Pin(soilData['dpin']))
        self.dry = soilData['dry']
        self.wet =  soilData['wet']
        self.numValuesAvg =  soilData['numValuesAvg']
        self.measureDuration = soilData['measureDuration']  # milliseconds
        self.numCalibrations = soilData['numCalibrations']
        
        self.sensor_values = []
        self.moisture_percentage = []
        self.last_measure_time = 0
        self.kalibration_loops = 0
        self.calibrated = True

    def map_range(self, value, from_min, from_max, to_max, to_min):
        from_range = from_max - from_min
        to_range = to_max - to_min
        scaled_value = (value - from_min) / from_range
        mapped_value = to_min + (scaled_value * to_range)
        return mapped_value
    
    def calibration(self):
        current_time = utime.ticks_ms()

        if 0 < self.kalibration_loops < self.numCalibrations:
            if current_time - self.last_measure_time >= 1000:  # 1 second in milliseconds
                sensor_value = self.adc.read()
                self.sensor_values.append(sensor_value)
                self.kalibration_loops += 1
                print("Calibration Running! {} Values left.".format(self.numCalibrations - self.kalibration_loops))
                self.last_measure_time = current_time

        elif self.kalibration_loops == 0:
            print("Attention, the sensor must be placed directly into water for calibration!")
            self.kalibration_loops += 1

        elif self.kalibration_loops == self.numCalibrations:
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
                
                

    def readMoisture(self):
        #print(self.last_measure_time)
        current_time = utime.ticks_ms()
        #print(current_time)
        #if current_time - self.last_measure_time >= self.measureDuration:
        for _ in range(self.numValuesAvg):
            sensor_value = self.adc.read()
            self.moisture_percentage.append(self.map_range(sensor_value, self.wet, self.dry, 0, 100))
            self.sensor_values.append(sensor_value)
            avg_percentage = sum( self.moisture_percentage) / len( self.moisture_percentage)
            avg_sensor_value = sum(self.sensor_values) / len(self.sensor_values)
            self.sensor_values.clear()
            self.moisture_percentage.clear()
            self.last_measure_time = current_time
            return avg_percentage #, avg_sensor_value
        #return None

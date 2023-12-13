from time import sleep_ms, ticks_ms 
from machine import I2C, Pin 
from i2c_lcd import I2cLcd 

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

def testLcd(num):
    lcd.move_to(3,0)
    lcd.putstr('Micropython')
    lcd.move_to(0,1)
    lcd.putstr("hello " + str(num))

if __name__ == '__main__':
    for i in range(100):
        testLcd(i)
        sleep_ms(200)
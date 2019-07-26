import serial
import time

ArduinoSerial=serial.Serial('COM4',9600)

def led_on():
        ArduinoSerial.write(b'1')

def led_off():
        ArduinoSerial.write(b'0')

print("1. Enter 1 to 'ON' \n2. Enter 0 to 'OFF'")
print("Enter here: ")
time.sleep(2)
#led_on()
while True:
        ip=input()
        if(ip=='1'):
                time.sleep(2)
                led_on()
        elif(ip=='0'):
                time.sleep(2)
                led_off()
        elif(ip=='q'):
                time.sleep(2)
                break




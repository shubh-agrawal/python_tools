# Drawback of using funtion readline() is that it always waits for newline charachter
# Documentation is available at http://pyserial.readthedocs.io/en/latest/shortintro.html

import serial,time
ser=serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=12)

s=ser.read(60)
print s
#time.sleep(3)

ser.close()

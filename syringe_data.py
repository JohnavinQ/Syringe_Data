import serial
import time

# Replace COM3 with your actual port
ser = serial.Serial('COM7', 115200, timeout=1)  # check baud rate on pump
time.sleep(2)  # wait for connection

ser.write(b'ivolume\r')  # send command
response = ser.read(100)  # read response

print("Pump response:", response.decode(errors='ignore'))

ser.close()
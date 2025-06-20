import serial
import time
import msvcrt  # For detecting keypress on Windows
import sys

# === Configuration ===
COM_PORT = 'COM7'         # Change this to match your actual COM port
BAUD_RATE = 115200         # Or whatever your pump is using
COMMAND = 'ivolume\r'     # Pump command (note: ends in \r, not \n)
LOG_FILENAME = sys.argv[1]
DELAY_SECONDS = 1         # Time between each query

# === Open Serial Connection ===
try:
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {COM_PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# === Open Log File ===
with open(LOG_FILENAME.txt, 'a') as logfile:
    print(f"Logging started. Writing to {LOG_FILENAME}")
    
    try:
        while True:
            # Stop if key is pressed
            if msvcrt.kbhit():
                print("Key pressed. Stopping logging.")
                break

            # Send IVOLUME command
            ser.write(COMMAND.encode())
            time.sleep(0.1)  # Give pump time to respond

            # Read response
            response = ser.readline().decode(errors='ignore').strip()

            if response:
                # Add timestamp
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"{timestamp} - {response}\n"
                logfile.write(log_entry)
                logfile.flush()  # Immediately write to disk
                print(log_entry.strip())
            
            time.sleep(DELAY_SECONDS)
    
    except KeyboardInterrupt:
        print("Interrupted by user.")

    finally:
        ser.close()
        print("Serial connection closed.")
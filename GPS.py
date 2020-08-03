import serial
with serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1) as ser:
	while True:
		try:
			line = ser.readline().decode('ascii', errors = 'replace')
			lines = line.split(",")
			if lines[0] == "$GPRMC":
				

import serial

import serial.tools.list_ports as port_list

# This will list available ports
ports = list(port_list.comports())
for p in ports:
    print(p)

# Communication through port
port = 'COM5'

bluetooth = serial.Serial(port=port, baudrate=115200, write_timeout=1)

bluetooth.flushInput()

bluetooth.write(b'hello, world\r\n')
bluetooth.close()

bluetooth.readline()

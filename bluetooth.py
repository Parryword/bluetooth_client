import serial

import serial.tools.list_ports as port_list


def scan():
    ports = list(port_list.comports())
    for p in ports:
        print(p)


class Bluetooth:
    def __init__(self, port='COM5', baud_rate=115200, timeout=1):
        # Communication through port
        self.bluetooth = serial.Serial(port=port, baudrate=baud_rate, write_timeout=timeout)

    def change_credentials(self):
        return

    def fetch_data(self):
        self.bluetooth.flushInput()
        self.bluetooth.write(b'hello, world\r\n')
        self.bluetooth.close()
        self.bluetooth.readline()
        return

import serial

import serial.tools.list_ports as port_list
import threading
import time


def scan():
    ports = list(port_list.comports())
    for p in ports:
        print(p)


class Bluetooth:
    def __init__(self, port='COM5', baud_rate=115200, timeout=1):
        try:
            self.bluetooth = serial.Serial(port=port, baudrate=baud_rate, write_timeout=timeout)
        except Exception as e:
            print("Failed to connect to ESP32.")
            print(e)

        # self.thread = threading.Thread(target=self.listen)
        # self.thread.start()

    def change_credentials(self, ssid: str, password: str):
        if not self.bluetooth.isOpen():
            self.bluetooth.open()
        self.bluetooth.flushInput()
        self.bluetooth.write(b'CRED -m ' + ssid.encode("ascii") + b'\r\n')
        data = self.bluetooth.readline()
        print(data.decode("ascii"))
        self.bluetooth.close()

    def fetch_data(self, city: str):
        if not self.bluetooth.isOpen():
            self.bluetooth.open()
        self.bluetooth.flushInput()
        self.bluetooth.write(b'FETCH\r\n')
        data = self.bluetooth.readline()
        print(data.decode("ascii"))
        self.bluetooth.close()

    def listen(self):
        while True:
            data = self.bluetooth.readline()
            print(data.decode("ascii"))
        # return data

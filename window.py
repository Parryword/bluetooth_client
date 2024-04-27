from tkinter import *
from tkinter import font
from bluetooth import *


class LabeledEntry(Entry):
    def __init__(self, master=None, label="Search", **kwargs):
        Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)


class App:
    connection = Bluetooth()
    temperature, humidity, wind_speed, sensor_temperature = 100, 101, 102, 103

    def __init__(self):
        green = "#a9cf7f"

        root = Tk()
        root.title("Weather Status")
        root.config(bg=green)
        root.resizable(False, False)

        # df = font.nametofont("TkDefaultFont")
        # df.config(size=20)

        left_frame = Frame(root, width=200, height=400)
        left_frame.grid(row=0, column=0, padx=10, pady=10)

        self.ssid_entry = LabeledEntry(left_frame, label="SSID")
        self.ssid_entry.grid(row=0, column=0, padx=10, pady=10)
        self.pass_entry = LabeledEntry(left_frame, label="Password")
        self.pass_entry.grid(row=1, column=0, padx=10, pady=10)
        submit_button = Button(left_frame, text="Submit", bg=green, fg="white", command=self.submit)
        submit_button.grid(row=2, column=0, padx=10, pady=10)

        right_frame = Frame(root, width=400, height=400)
        right_frame.grid(row=0, column=1, padx=10, pady=10)

        update_button = Button(right_frame, text="Update", bg=green, fg="white", command=self.update)
        update_button.grid(row=2, column=0, padx=10, pady=10)

        main_header = Label(right_frame, text="Current Weather")
        main_header.grid(row=0, column=0, padx=10, pady=10)

        weather_frame = Frame(right_frame)
        weather_frame.grid(row=1, column=0, padx=10, pady=10)

        temp_header = Label(weather_frame, text="Temperature")
        temp_header.grid(row=1, column=0, padx=10, pady=10)
        humidity_header = Label(weather_frame, text="Humidity")
        humidity_header.grid(row=2, column=0, padx=10, pady=10)
        wind_header = Label(weather_frame, text="Wind speed")
        wind_header.grid(row=3, column=0, padx=10, pady=10)
        sensor_header = Label(weather_frame, text="Sensor temp.")
        sensor_header.grid(row=4, column=0, padx=10, pady=10)

        temp_val_header = Label(weather_frame, text=str(self.temperature))
        temp_val_header.grid(row=1, column=1, padx=10, pady=10)
        humidity_val_header = Label(weather_frame, text=str(self.humidity))
        humidity_val_header.grid(row=2, column=1, padx=10, pady=10)
        wind_val_header = Label(weather_frame, text=str(self.wind_speed))
        wind_val_header.grid(row=3, column=1, padx=10, pady=10)
        sensor_val_header = Label(weather_frame, text=str(self.sensor_temperature))
        sensor_val_header.grid(row=4, column=1, padx=10, pady=10)

        root.mainloop()

    def submit(self):
        ssid = self.ssid_entry.get()
        password = self.pass_entry.get()
        self.connection.change_credentials(ssid, password)

    def update(self):
        self.connection.fetch_data()


if __name__ == '__main__':
    scan()
    App()

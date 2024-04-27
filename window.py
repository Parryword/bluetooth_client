from tkinter import *


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


green = "#a9cf7f"

root = Tk()
root.title("Weather Status")
root.config(bg=green)

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=10)

ssid_entry = LabeledEntry(left_frame, label="SSID")
ssid_entry.grid(row=0, column=0, padx=10, pady=10)
pass_entry = LabeledEntry(left_frame, label="Password")
pass_entry.grid(row=1, column=0, padx=10, pady=10)
submit_button = Button(left_frame, text="Submit", bg=green, fg="white")
submit_button.grid(row=2, column=0, padx=10, pady=10)

right_frame = Frame(root, width=400, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=10)
root.mainloop()

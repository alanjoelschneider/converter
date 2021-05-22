import tkinter as tk
from tkinter import ttk
import converters

class BaseConverter(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.configure(padx=10, pady=10)
    self.pack()

    self.bases = {"Decimal": "d", "Binario": "b", "Hexadecimal": "h"}
    self.converters = {
      "bd": converters.binToDec,
      "bh": converters.binToHex,
      "db": converters.decToBin,
      "dh": converters.decToHex,
      "hd": converters.hexToDec,
      "hb": converters.hexToBin
    }

    self.leftEntryValue = tk.StringVar()
    self.leftComboBoxValue = tk.StringVar()
    self.rightEntryValue = tk.StringVar()
    self.rightComboBoxValue = tk.StringVar()
    self.leftEntryValue.trace('w', self.convert)

    self.__initWidgets__()

  def __initWidgets__(self):
    self.leftComboBox = ttk.Combobox(self, textvariable=self.leftComboBoxValue)
    self.leftComboBox.grid(column=0, row=0)
    self.leftComboBox.set("Decimal")
    self.leftComboBox["values"] = list(self.bases.keys())
    self.leftComboBox["state"] = "readonly"
    self.leftComboBox.bind('<<ComboboxSelected>>', self.convert)

    self.rightComboBox = ttk.Combobox(self, textvariable=self.rightComboBoxValue)
    self.rightComboBox.grid(column=1, row=0)
    self.rightComboBox.set("Binario")
    self.rightComboBox["values"] = list(self.bases.keys())
    self.rightComboBox["state"] = "readonly"
    self.rightComboBox.bind('<<ComboboxSelected>>', self.convert)

    self.leftEntry = ttk.Entry(self, textvariable=self.leftEntryValue)
    self.leftEntry.grid(column=0, row=1, sticky="w")
    self.leftEntry.focus()

    self.rightEntry = ttk.Entry(self, textvariable=self.rightEntryValue)
    self.rightEntry["state"] = "readonly"
    self.rightEntry.grid(column=1, row=1, sticky="w")

    self.switchButton = ttk.Button(self, text="Switch", command=self.switch)
    self.switchButton.grid(column=2, row=0)

  def convert(self, *args):
    if (self.leftEntryValue.get()):
      try:
        leftBase = self.bases[self.leftComboBoxValue.get()]
        rightBase = self.bases[self.rightComboBoxValue.get()]
        converter = self.converters[f"{leftBase}{rightBase}"]
        result = converter(self.leftEntryValue.get())
        self.rightEntryValue.set(result)
      except:
        print("[Error]: Invalid values.")
    else:
      self.rightEntryValue.set("")

  def switch(self):
    # switch values between combos
    temp = self.leftComboBoxValue.get()
    self.leftComboBoxValue.set(self.rightComboBox.get())
    self.rightComboBox.set(temp)

    # switch values between entries
    temp = self.leftEntryValue.get()
    self.leftEntryValue.set(self.rightEntryValue.get())
    self.rightEntryValue.set(temp)

    self.convert()



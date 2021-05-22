import tkinter as tk
from tkinter import ttk
from BaseConverter import BaseConverter

def main():
  app = tk.Tk()
  app.title("Converter")
  app.resizable(False, False)

  BaseConverter(app)
  BaseConverter(app)
  BaseConverter(app)

  app.mainloop()

if __name__ == "__main__":
  main()
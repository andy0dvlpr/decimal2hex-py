import tkinter as tk
from tkinter import messagebox # messagebox isn't always imported by default for some reason.

def show_result():
    tk.messagebox.showinfo(title="Result", message="Hexadecimal: %x" % int(entry.get()))
    # Shows an info type message box with the input of the entry in the tk window as an integer in hexadecimal form.

master = tk.Tk()
master.title("Decimal to Hexadecimal Converter")

tk.Label(master, text="Decimal:").grid(row=0)
entry = tk.Entry(master)
entry.grid(row=0, column=1)

tk.Button(master, text="Quit", command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text="Show", command=show_result).grid(row=3, column=1, sticky=tk.W, pady=4)

master.mainloop()
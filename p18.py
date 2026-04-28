# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:00:02 2026

@author: Christian Bahamon
"""
import tkinter as tk

def calculate():
    kelvin = entry_kelvin.get()

    entry_kelvin.config(bg="white")
    entry_error.config(bg="white")
    entry_error.delete(0, tk.END)

    if kelvin == "":
        show_error("Input cannot be blank")
        return

    try:
        kelvin = float(kelvin)
    except:
        show_error("Must be a number")
        return

    if kelvin <= 0:
        show_error("Kelvin must be greater than 0")
        return

    # Conversion
    celsius = kelvin - 273.15
    fahrenheit = (9/5) * (kelvin - 273) + 32

    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.delete(0, tk.END)

    entry_celsius.insert(0, f"{celsius:.2f}")
    entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")


def show_error(message):
    entry_error.insert(0, message)
    entry_error.config(bg="red")
    entry_kelvin.config(bg="red")


def clear_all():
    entry_kelvin.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.delete(0, tk.END)
    entry_error.delete(0, tk.END)

    entry_kelvin.config(bg="white")
    entry_error.config(bg="white")



root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("400x350")

tk.Label(root, text="Temperature Conversion", font=("Arial", 20)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Kelvin:").grid(row=0, column=0, pady=5)
tk.Label(frame, text="Celsius:").grid(row=1, column=0, pady=5)
tk.Label(frame, text="Fahrenheit:").grid(row=2, column=0, pady=5)

entry_kelvin = tk.Entry(frame)
entry_celsius = tk.Entry(frame)
entry_fahrenheit = tk.Entry(frame)

entry_kelvin.grid(row=0, column=1)
entry_celsius.grid(row=1, column=1)
entry_fahrenheit.grid(row=2, column=1)


entry_error = tk.Entry(root, width=40)
entry_error.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="CALCULATE", width=10, command=calculate).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="CLEAR", width=10, command=clear_all).grid(row=0, column=1, padx=5)

tk.Button(root, text="QUIT", width=10, command=root.destroy).pack(pady=5)

root.mainloop()


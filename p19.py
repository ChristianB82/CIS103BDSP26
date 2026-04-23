# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:20:06 2026

@author: chris
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Graphics Assignment")
    
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    canvas.create_oval(50, 50, 250, 250, outline="green", width=2)

    canvas.create_oval(80, 80, 120, 120, fill="red")

    canvas.create_oval(180, 80, 220, 120, fill="blue")

    canvas.create_rectangle(120, 150, 180, 160, fill="yellow")

    canvas.create_polygon(120, 220, 180, 220, 150, 270, outline="black", fill="", width=3)

    root.mainloop()

main()
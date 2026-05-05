# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:18:05 2026

@author: Christian Bahamon"""

import turtle

def main():
    
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    screen.setup(width=400, height=400)
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.color("green")
    pen.circle(100)

    pen.penup()
    pen.goto(-40, 20)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

    pen.penup()
    pen.goto(40, 20)
    pen.pendown()
    pen.color("blue")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

    pen.penup()
    pen.goto(-50, 0)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(100)
        pen.right(90)
        pen.forward(10)
        pen.right(90)
    pen.end_fill()

    pen.penup()
    pen.goto(-30, -70)
    pen.pendown()
    pen.color("black")
    pen.pensize(15)

    pen.goto(40, -70)
    pen.goto(0, -120)
    pen.goto(-40, -70)

    pen.hideturtle()
    screen.mainloop()

main()

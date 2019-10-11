# Turtle Flowers

import turtle as t

def spiral1():
    t.pencolor('green')
    t.speed(100)
    for i in range(100):
        t.forward(100)
        t.right(92)
        t.penup()
        t.pendown()

def spiral2():
    t.pencolor('red')
    t.speed(100)
    for i in range(100):
        t.forward(150)
        t.left(95)
        t.penup()
        t.pendown()

def spiral3():
    t.pencolor('blue')
    t.speed(100)
    for i in range(100):
        t.forward(100)
        t.left(105)
        t.penup()
        t.pendown()

def spiral4():
    t.pencolor('orange')
    t.speed(100)
    for i in range(100):
        t.forward(150)
        t.left(100)
        t.penup
        t.pendown()


spiral1()
t.penup()
t.setpos(0,100)
spiral2()
t.penup()
t.setpos(0,-100)
spiral3()
t.penup()
t.setpos(100,-100)
spiral4()
t.penup()
t.setpos(-300,100)
t.pencolor('black')
t.color('purple')
t.write('Turtle Flowers', font=("Serif", 26, 'normal', 'bold', 'italic', 'underline'))
t.setpos(-300,50)
t.write('by Don Watkins', font=("Serif", 22, 'normal', 'bold', 'italic', 'underline'))

from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon (): 
    color("blue")
    dot(diameter)

def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("TURTLE!")

        
draw_balloon()

onkey(inflate_balloon, "Up")
listen()
 
done()
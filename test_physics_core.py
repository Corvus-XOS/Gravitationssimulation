# Testen von physics_core.py
#
# Autor: Jonas

import physics_core as pc
# import numpy as np
import math
from turtle import Turtle

# planet1 = pc.Planet(x_pos=50, y_pos=0, masse=1e15, speed=30, degree=150)
# planet2 = pc.Planet(x_pos=-25, y_pos=43.3, masse=1e15, speed=30, degree=270)
# planet3 = pc.Planet(x_pos=-25, y_pos=-43.3, masse=1e15, speed=30, degree=30)

v = 28

planet1 = pc.Planet(x_pos=50, y_pos=0, masse=1e15, speed=v, degree=90)
planet2 = pc.Planet(x_pos=-25, y_pos=50 * math.sin(math.radians(120)), masse=1e15, speed=v, degree=210)
planet3 = pc.Planet(x_pos=-25, y_pos=-50 * math.sin(math.radians(120)), masse=1e15, speed=v, degree=330)

# planet1 = pc.Planet(masse=1e15)
# planet2 = pc.Planet(y_pos=50, masse=1e15, speed=36.53568)

planet_arr = [planet1, planet2, planet3]
# planet_arr = [planet1, planet2]
# planet_np = np.array(planet_arr)




t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.shape("circle")
t2.shape("circle")
t3.shape("circle")


t1.showturtle()
t2.showturtle()
t3.showturtle()

t1.penup()
t2.penup()
t3.penup()

while True:
    for j in range(0, 200):
        pc.update(arr=planet_arr, n=len(planet_arr))

    # print(planet_arr[0].x_spd, planet_arr[0].y_spd, planet_arr[1].x_spd, planet_arr[1].y_spd)

    t1.goto(planet_arr[0].x_pos, planet_arr[0].y_pos)
    t2.goto(planet_arr[1].x_pos, planet_arr[1].y_pos)
    t3.goto(planet_arr[2].x_pos, planet_arr[2].y_pos)
    t1.pendown()
    t2.pendown()
    t3.pendown()


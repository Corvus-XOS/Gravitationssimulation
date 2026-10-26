# Testen von physics_core.py
#
# Autor: Jonas

import physics_core as pc
import numpy as np
from turtle import Turtle

planet1 = pc.Planet(x_pos=50, y_pos=0, masse=1e15, speed=30, degree=150)
planet3 = pc.Planet(x_pos=-25, y_pos=43.3, masse=1e15, speed=30, degree=270)
planet2 = pc.Planet(x_pos=-25, y_pos=-43.3, masse=1e15, speed=30, degree=30)

# planet1 = pc.Planet(masse=1e15)
# planet2 = pc.Planet(y_pos=50, masse=1e0, speed=36.53568)

planet_arr = [planet1, planet2, planet3]
# planet_arr = [planet1, planet2]
planet_np = np.array(planet_arr)

# planet_arr[0].update(planet_arr, n=5 , i=1)



t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.shape("circle")
t2.shape("circle")
t3.shape("circle")

t1.speed(100)
t2.speed(100)
t3.speed(100)


t1.showturtle()
t2.showturtle()
t3.showturtle()

t1.penup()
t2.penup()
t3.penup()

while True:
    for j in range(0, 2000):
        pc.update(arr=planet_arr, n=len(planet_arr))
        print(planet_arr[0].pos)
        # for i in range(0, len(planet_arr) - 1):
        # for i in range(0,len(planet_arr)):
        #     pc.update_pos(arr=planet_arr, i=i)

        # print(planet_arr[0].x_spd, planet_arr[0].y_spd, planet_arr[1].x_spd, planet_arr[1].y_spd)



    # # t1.goto(planet_arr[0].x_pos, planet_arr[0].y_pos)
    # t1.goto(planet_arr[0].pos[0], planet_arr[0].pos[1])
    # # t2.goto(planet_arr[1].x_pos, planet_arr[1].y_pos)
    # t2.goto(planet_arr[1].pos)
    # # t3.goto(planet_arr[2].x_pos, planet_arr[2].y_pos)
    # t3.goto(planet_arr[2].pos)
    # t1.pendown()
    # t2.pendown()
    # t3.pendown()


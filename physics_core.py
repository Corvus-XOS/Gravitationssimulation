# Physik Berechnungen 
#
# Autor: Jonas

import numpy as np

G = 6.67430e-11 # m^3 / kg * s^2
dt = 1e-3 # s


class Planet:
    def __init__(self, masse: float=1 , x_pos: float=0, y_pos: float=0, speed: float=0, degree: float=0):
        self.masse = masse # kg
        self.x_pos = x_pos # m
        self.y_pos = y_pos # m
        self.x_spd = speed * np.cos(np.deg2rad(degree)) # m/s
        self.y_spd = speed * np.sin(np.deg2rad(degree)) # m/s
        self.dx_spd = 0 # m/s
        self.dy_spd = 0 # m/s

def update(arr: list["Planet"], n: int, i: int):
    for j in range(i + 1, n):
        # if (j != i):
        # r = np.hypot(arr[i].x_pos - arr[j].x_pos, arr[i].y_pos - arr[j].y_pos)
        dx = arr[j].x_pos - arr[i].x_pos
        dy = arr[j].y_pos - arr[i].y_pos
        F = G * arr[i].masse * arr[j].masse / (np.pow(dx, 2) + np.pow(dy, 2))

        alpha = np.arctan2(-dy, -dx)
        dx_spd = F * dt * np.cos(alpha)
        dy_spd = F * dt * np.sin(alpha)



        arr[i].dx_spd -= dx_spd / arr[i].masse
        arr[i].dy_spd -= dy_spd / arr[i].masse

        arr[j].dx_spd += dx_spd / arr[j].masse
        arr[j].dy_spd += dy_spd / arr[j].masse




def update_pos(arr: list["Planet"], i: int):
    arr[i].x_spd += arr[i].dx_spd
    arr[i].y_spd += arr[i].dy_spd

    arr[i].x_pos += arr[i].x_spd * dt
    arr[i].y_pos += arr[i].y_spd * dt

    arr[i].dx_spd = 0
    arr[i].dy_spd = 0

    # arr[j].x_pos += arr[j].x_spd * dt
    # arr[j].y_pos += arr[j].y_spd * dt

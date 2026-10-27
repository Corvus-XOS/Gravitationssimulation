# Physik Berechnungen 
#
# Autor: Jonas

# import numpy as np
import math

G = 6.67430e-11 # m^3 / kg * s^2
dt = 1e-4 # s


class Planet:
    def __init__(self, masse: float=1 , x_pos: float=0, y_pos: float=0, speed: float=0, degree: float=0, color: str="black"):
        self.masse = masse # kg
        self.x_pos = x_pos # m
        self.y_pos = y_pos # m
        rad = math.radians(degree)
        self.x_spd = speed * math.cos(rad) # m/s
        self.y_spd = speed * math.sin(rad) # m/s
        self.dx_spd = 0.0 # m/s
        self.dy_spd = 0.0 # m/s
        self.color = color

def update(arr: list["Planet"], n: int):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # Berechnung der Kräfte
            dx = arr[i].x_pos - arr[j].x_pos
            dy = arr[i].y_pos - arr[j].y_pos
            r = math.sqrt(dx**2 + dy**2)
            F = G * arr[i].masse * arr[j].masse / r**3

            dx_spd = F * dt * dx
            dy_spd = F * dt * dy

            # Berechung Geschwindigkeitsänderung
            arr[i].dx_spd -= dx_spd / arr[i].masse
            arr[i].dy_spd -= dy_spd / arr[i].masse

            arr[j].dx_spd += dx_spd / arr[j].masse
            arr[j].dy_spd += dy_spd / arr[j].masse

    # Aktualisierung der Positionen
    update_pos(arr=arr, n=n)




def update_pos(arr: list["Planet"], n: int):
    for i in range(0, n):
        arr[i].x_spd += arr[i].dx_spd
        arr[i].y_spd += arr[i].dy_spd

        arr[i].x_pos += arr[i].x_spd * dt
        arr[i].y_pos += arr[i].y_spd * dt

        arr[i].dx_spd = 0.0
        arr[i].dy_spd = 0.0

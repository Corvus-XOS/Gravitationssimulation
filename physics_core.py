# Physik Berechnungen 
#
# Autor: Jonas

import math
from auxFile import MassObject

# Gravitationskonstante
G = 6.67430e-11 # m^3 / kg * s^2


def update(arr: list["MassObject"], n: int, dt: float):
    for i in range(0, n - 1): 
        for j in range(i + 1, n):
            # Berechnung der Kräfte
            dx = arr[i].x_pos - arr[j].x_pos
            dy = arr[i].y_pos - arr[j].y_pos
            r = math.sqrt(dx**2 + dy**2)

            # Berechung Geschwindigkeitsänderung zwischen beiden Objekten
            # v = (G * m1 * m2) / (r^3) * rx * dt * mx
            F = G * arr[i].mass * arr[j].mass / r**3

            dx_spd = F * dt * dx
            dy_spd = F * dt * dy

            arr[i].dx_spd -= dx_spd / arr[i].mass
            arr[i].dy_spd -= dy_spd / arr[i].mass

            arr[j].dx_spd += dx_spd / arr[j].mass
            arr[j].dy_spd += dy_spd / arr[j].mass

    # Aktualisierung der Positionen nch brechnung der Geschwindigkeit
    update_pos(arr=arr, n=n, dt=dt)


def update_pos(arr: list["MassObject"], n: int, dt: float):
    for i in range(0, n):
        # Aktualisierung der Geschwindigkeit aus Geschwindigkeitsänderung
        arr[i].x_spd += arr[i].dx_spd
        arr[i].y_spd += arr[i].dy_spd

        # Aktualisierung der Position aus Geschwindigkeit
        arr[i].x_pos += arr[i].x_spd * dt
        arr[i].y_pos += arr[i].y_spd * dt

        arr[i].dx_spd = 0.0
        arr[i].dy_spd = 0.0

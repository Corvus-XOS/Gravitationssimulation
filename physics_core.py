# Physik Berechnungen 
#
# Autor: Jonas

import numpy as np

G = 6.67430e-11 # m^3 / kg * s^2
dt = 1e-3 # s


class Planet:
    def __init__(self, masse: float=1 , x_pos: float=0, y_pos: float=0, speed: float=0, degree: float=0):
        self.masse = masse # kg
        # self.x_pos = x_pos # m
        # self.y_pos = y_pos # m
        self.pos = np.array([x_pos, y_pos], dtype=np.float64)
        # self.x_spd = speed * np.cos(np.deg2rad(degree)) # m/s
        # self.y_spd = speed * np.sin(np.deg2rad(degree)) # m/s
        self.v = np.array([speed * np.cos(np.deg2rad(degree)),speed * np.sin(np.deg2rad(degree))], dtype=np.float64)
        # self.dx_spd = 0 # m/s
        # self.dy_spd = 0 # m/s
        self.dv = np.array([0, 0], dtype=np.float64)

def update(arr: list["Planet"], n: int):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # if (j != i):
            # r = np.hypot(arr[i].x_pos - arr[j].x_pos, arr[i].y_pos - arr[j].y_pos)
            # dx = arr[j].x_pos - arr[i].x_pos
            # dy = arr[j].y_pos - arr[i].y_pos
            d_pos = arr[i].pos - arr[j].pos
            F = G * arr[i].masse * arr[j].masse / (np.pow(d_pos[0], 2) + np.pow(d_pos[1], 2))

            # alpha = np.arctan2(-dy, -dx)
            alpha = np.arctan2(d_pos[0], d_pos[1])
            # dx_spd = F * dt * np.cos(alpha)
            # dy_spd = F * dt * np.sin(alpha)
            dv = F * dt * np.array([np.cos(alpha), np.sin(alpha)])


            # arr[i].dx_spd -= dx_spd / arr[i].masse
            # arr[i].dy_spd -= dy_spd / arr[i].masse
            arr[i].dv -= dv / arr[i].masse

            # arr[j].dx_spd += dx_spd / arr[j].masse
            # arr[j].dy_spd += dy_spd / arr[j].masse
            arr[j].dv += dv / arr[j].masse

    update_pos(arr=arr, n=n)




def update_pos(arr: list["Planet"], n: int):
    for i in range(0,n):
        # arr[i].x_spd += arr[i].dx_spd
        # arr[i].y_spd += arr[i].dy_spd
        arr[i].v += arr[i].dv

        # arr[i].x_pos += arr[i].x_spd * dt
        # arr[i].y_pos += arr[i].y_spd * dt
        arr[i].pos += arr[i].dv * dt

        # speed_arr = np.array([arr[i].x_spd, arr[i].y_spd])
        # arr[i].pos += speed_arr * dt

        # arr[i].dx_spd = 0
        # arr[i].dy_spd = 0
        arr[i].dv = 0

    # arr[j].x_pos += arr[j].x_spd * dt
    # arr[j].y_pos += arr[j].y_spd * dt

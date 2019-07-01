#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## 101
## File description:
## task
##

from math import *

import sys
import math

def calculating_velocity(liste):
    print("The velocity vector of the ball is:")
    x1 = d - a
    y1 = e - b
    z1 = f - c
    print('('+"{:.2f}".format(x1)+',', "{:.2f}".format(y1)+',', "{:.2f}".format(z1)+')')

def calculating_coordinates(liste):
    print("At time t +",g, "ball coordinates will be:")
    xn = (d - a) * (g + 1) + a
    yn = (e - b) * (g + 1) + b
    zn = (f - c) * (g + 1) + c
    print('('+"{:.2f}".format(xn)+',', "{:.2f}".format(yn)+',', "{:.2f}".format(zn)+')')

def calculating_norm_and_angle(liste):
    x1 = (d - a) * (d - a)
    y1 = (e - b) * (e - b)
    z1 = (f - c) * (f - c)
    norme = sqrt(x1 + y1 + z1)
    z1 = sqrt(z1)
    p = z1 / norme
    s = math.pi/2
    rad = (acos(p)) - s
    degres = abs((rad*180)/math.pi)
    return degres

def printing(degres):
    if c > 0 and f > 0 or c < 0 and f < 0:
        print("The incidence angle is:")
        print("{0:.2f}".format(degres),"degrees")
    elif c > 0 and f < 0 or c < 0 and f > 0:
        print("The ball won't reach the bat.")
    
if __name__ == '__main__':
    if len(sys.argv) != 8:
        exit (84)
    elif int(sys.argv[7]) < 0:
        exit (84)

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    e = float(sys.argv[5])
    f = float(sys.argv[6])
    g = int(sys.argv[7])
    liste = [a, b, c, d, e, f, g]
    h = 0
            
    calculating_velocity(liste)
    calculating_coordinates(liste)
    degres = calculating_norm_and_angle(liste)
    printing(degres)

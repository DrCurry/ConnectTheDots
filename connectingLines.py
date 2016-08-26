import math
import pygame as p
import random
import sys
import time
from pygame.locals import *

width = 1280
height = 720
numCircles = 400
radius = 5
delay = .001
distanceBtwn = 100

upperMultiplier = .98  # upper \
#                               equals 1
lowerMultiplier = .02  # lower /

p.display.init()
screen = p.display.set_mode((width, height), 0, 32)

dist = [0 for e in range(numCircles)]


def timer(seconds):
    time.sleep(seconds)


def update():
    p.display.update()


BACKGROUND = (127, 127, 127)
COLOR1 = (255, 0, 0)
COLOR2 = (0, 255, 0)
COLOR3 = (0, 0, 255)
COLOR4 = (21, 255, 200)
COLOR5 = (30, 200, 50)
screen.fill(BACKGROUND)

# creates a maximum and minimum range where points are to be located
# prevents points from being draw near the edge of screen (neatness factor)
randWidthUpper = int(width * upperMultiplier)
randWidthLower = int(width * lowerMultiplier)
randHeightUpper = int(height * upperMultiplier)
randHeightLower = int(height * lowerMultiplier)

X_Points = [0 for x in range(numCircles)]
Y_Points = [0 for x in range(numCircles)]

for i in range(0, numCircles):  # creates x and y coordinates within the boundaries
    X_Points[i] = random.randint(randWidthLower, randWidthUpper)
    Y_Points[i] = random.randint(randHeightLower, randHeightUpper)

for i in range(0, numCircles):  # makes circles
    p.draw.circle(screen, COLOR1, (X_Points[i], Y_Points[i]), radius)
    update()
    p.event.pump()  # allows the window to be moved will executing
    timer(delay)

for i in range(0, numCircles - 1):
    timer(delay)
    for j in range(0, numCircles - 1):

        # distance formula
        dist[i] = math.sqrt(((X_Points[i] - X_Points[j + 1]) ** 2) + ((Y_Points[i] - Y_Points[j + 1]) ** 2))
        if (dist[i] < distanceBtwn):  # connects all points that are less than distanceBtwn
            p.draw.line(screen, COLOR3, (X_Points[i], Y_Points[i]), (X_Points[j + 1], Y_Points[j + 1]), 1)
            timer(delay)
            update()

    p.event.pump()

while True:
    for event in p.event.get():
        if event.type == QUIT:
            p.display.quit()
            sys.exit()

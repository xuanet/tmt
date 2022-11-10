import turtle

import numpy as np
import turtle as t
import random

def getNewPoint(current):
    angle = random.uniform(0, 2*np.pi)
    mag = random.randrange(100, 200)
    newX = current[0] + (mag*np.cos(angle))
    newY = current[1] + (mag*np.sin(angle))
    while checkXPointinBounds(newX) == False or checkYPointinBounds(newY) \
            == False:
        angle = random.uniform(0, 2*np.pi)
        mag = random.randrange(4*r, 8*r)
        newX = current[0] + (mag * np.cos(angle))
        newY = current[1] + (mag * np.sin(angle))
    return [int(newX), int(newY)]

def checkXPointinBounds(x):
    return 0+r < x < maxX-r

def checkYPointinBounds(y):
    return 0+r < y < maxY-r

def checkPoint(point):
    for i in points:
        if distance(i, point) < 3*r:
            return False
    return True


def distance(p1, p2):
    xsquare = (p1[0] - p2[0])**2
    ysquare = (p1[1] - p2[1])**2
    return (xsquare + ysquare)**0.5


maxX = 800/5
maxY = 1000/5
r = 30/5

firstX = random.uniform(0+r, maxX-r)
firstY = random.uniform(0+r, maxY-r)

points = [[int(firstX), int(firstY)]]


for k in range(1, 25):
    newPoint = getNewPoint(points[k-1])
    while checkPoint(newPoint) == False:
        newPoint = getNewPoint(points[k-1])
    points.append(newPoint)


points = sorted(points, key = lambda x: x[0])

adjustedpoints = [[5*x[0], 5*x[1]] for x in points]
print(adjustedpoints)


win = t.Screen()
t.screensize(maxX, 2*maxY)


brad = turtle.Turtle()

turtle.speed(0)

turtle.goto(0,0)
turtle.goto(maxX,0)
turtle.goto(maxX,maxY)
turtle.goto(0,maxY)
turtle.goto(0,0)

brad.penup()
brad.goto(points[0][0], points[0][1]-r)
brad.pendown()
brad.circle(r)
brad.penup()

print("WE ARE NOW HERE")

for i in range(1, len(points)):
    brad.goto(points[i][0], points[i][1]-r)
    brad.pendown()
    brad.circle(r)
    brad.penup()

win.exitonclick()


from time import sleep
from lib/stepper import Stepper

xStepper = Stepper(0, 0, 0, 0)
yStepper = Stepper(0, 0, 0, 0)

servo = None

#Global
DELAY = 2
CM_MOVE = 120

#functions
def getChangeXY(start = (0,0), end = (0,0)):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    sx = 1 if dx>=0 else -1
    sy = 1 if dy>=0 else -1
    return (dx if dx>=0 else -dx, dy if dy>=0 else -dy, sx, sy)


def moveXY(start = (0,0), end = (0,0)):
    dx, dy, sx, sy = getChangeXY(start, end)
    mx = CM_MOVE * dx
    my = CM_MOVE * dy
    tx = DELAY if mx>=my else DELAY*(dx/dy)
    ty = DELAY if my>=mx else DELAY*(dy/dx)

    xStepper.asyncMove(xStepper, (mx))
    yStepper.asyncMove(yStepper, (my))

    #wait for motion to complete
    duration = tx if tx>ty else ty
    sleep(duration/1000)

def transition(start, end):
    penUp()
    moveXY(start, end)
    penDown()
    sleep(1)

def penUp():
    #servo up
    pass

def penDown():
    #servo down
    pass

def changeLine(current, next):
    pass

"""
[ #Schema
    [ #Line
        [(0,0), (2,5)], #Segment
        [(2,5), (4,-3)] #Segment
    ],
    [ #Line
        [(0,0), (2,5)], #Segment
        [(2,5), (4,-3)]
    ]
]
"""

def draw(schema):
    for line in schema:
        for i in range(len(line)):
            segment = line[i]
            if(i == len(line)-1):
                changeLine()
            moveXY(segment[0], segment[1])
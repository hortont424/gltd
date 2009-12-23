from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

def drawCircle(x, y, rad):
    for r in range (0, 360):
        i = float(radians(r))
        glVertex2f(rad * cos(i) + x, rad * sin(i) + y)
    glVertex2f(rad * cos(0) + x, rad * sin(0) + y)

def drawLine(x1, y1, x2, y2, width):
    half = float(width) / 2.0
    if(x1 == x2):
        if y2 > y1:
            y1 += width
            y2 -= width
        else:
            y1 -= width
            y2 += width
        glVertex2f(float(x1 + half), float(y1 - half))
        glVertex2f(float(x1 - half), float(y1 - half))
        glVertex2f(float(x2 - half), float(y2 + half))
        glVertex2f(float(x2 + half), float(y2 + half))
    elif(y1 == y2):
        if x2 > x1:
            x1 -= width
            x2 += width
        else:
            x1 += width
            x2 -= width
        glVertex2f(float(x1 + half), float(y1 + half))
        glVertex2f(float(x1 + half), float(y1 - half))
        glVertex2f(float(x2 - half), float(y2 - half))
        glVertex2f(float(x2 - half), float(y2 + half))

def drawRect(x, y, w, h, t):
    drawLine(x, y, x, y + h, t)
    drawLine(x, y + h, x + w, y + h, t)
    drawLine(x + w, y, x + w, y + h, t)
    drawLine(x, y, x + w, y, t)
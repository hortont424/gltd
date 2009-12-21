from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

def circle(k, r, h):
    glBegin(GL_LINES)
    for i in range (0, 180):
        glVertex3f(r * cos(i) - h + k, r * sin(i) + k - h)
        glVertex3f(r * cos(i + 0.01) - h + k, r * sin(i + 0.01) + k - h)
    glEnd()
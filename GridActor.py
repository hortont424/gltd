from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

class GridActor(Actor):
    def __init__(self, x, y):
        super(GridActor, self).__init__(x, y)
    
    def draw(self, rect):
        glPushMatrix()
        
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 100.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(100.0, 100.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(100.0, 0.0, 0.0)
        glEnd()
        
        glPopMatrix()
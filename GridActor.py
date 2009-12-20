from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

class GridActor(Actor):
    def __init__(self):
        super(GridActor, self).__init__(0, 0)
        self.gridWidth = 15
        self.gridHeight = 15
    
    def draw(self, rect):
        glPushMatrix()
        
        glBegin(GL_QUADS)
        glColor3f(0.000, 0.145, 0.384)
        glVertex2f(0.0, 0.0)
        glVertex2f(self.window.width, 0.0)
        glColor3f(0.204, 0.396, 0.643)
        glVertex2f(self.window.width, self.window.height)
        glVertex2f(0, self.window.height)
        glEnd()
        
        glLineWidth(0.1)
        glColor4f(0.447, 0.624, 0.812, 0.8)

        glBegin(GL_LINES)
        
        for i in range(0, self.gridWidth):
            x = (self.window.width / self.gridWidth) * i
            glVertex2f(x, 0)
            glVertex2f(x, self.window.height)

        for i in range(0, self.gridHeight):
            y = (self.window.height / self.gridHeight) * i
            glVertex2f(0, y)
            glVertex2f(self.window.width, y)
        
        glEnd()
        
        glPopMatrix()
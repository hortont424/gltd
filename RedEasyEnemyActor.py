from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from EnemyActor import *
from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

class RedEasyEnemyActor(EnemyActor):
    def render(self):
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glColor4f(1.0, 0.0, 0.0, 0.9)

        glBegin(GL_QUADS)
        
        glVertex2f(10, 10)
        glVertex2f(10, self.height - 10)
        glVertex2f(self.width - 10, self.height - 10)
        glVertex2f(self.width - 10, 10)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
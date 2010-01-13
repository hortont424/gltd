from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Animation import *
from Actor import *
from GroupActor import *

from Utilities import *

class TowerChooser(GroupActor):
    def __init__(self, x, y, w, h):
        super(TowerChooser, self).__init__(x, y, w, h)
    
    def render(self):
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        inset = 10.0

        glBegin(GL_QUADS)
        
        glColor4f(0.004, 0.196, 0.443, 1.0)
        glVertex2f(self.width - inset, 0.0 + inset)
        glVertex2f(0.0 + inset, 0.0 + inset)
        glColor4f(0.304, 0.496, 0.743, 1.0)
        glVertex2f(0.0 + inset, self.height - inset)
        glVertex2f(self.width - inset, self.height - inset)
        
        glColor4f(0.304, 0.496, 0.743, 1.0)
        drawRect(0.0 + inset, 0.0 + inset, self.width - (inset * 2), self.height - (inset * 2), 2)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()

    def draw(self):
        self.validate()
        glCallList(self.displayList)
        
        super(TowerChooser, self).draw()
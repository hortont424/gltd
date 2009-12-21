from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *
from GridActor import gridWidth, gridHeight

class EnemyActor(Actor):
    def __init__(self, x, y):
        super(EnemyActor, self).__init__(0, 0, 0, 0)
        
        self.gridX = x
        self.gridY = y
        
        self.initialPositionSet = False
    
    def render(self):
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glColor4f(0.0, 0.0, 0.0, 1.0)

        glBegin(GL_QUADS)
        
        glVertex2f(0, 0)
        glVertex2f(0, self.height)
        glVertex2f(self.width, self.height)
        glVertex2f(self.width, 0)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)

    def updatePosition(self):
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        if not self.initialPositionSet:
            self.x = self.width * self.gridX
            self.y = self.height * self.gridY
            self.initialPositionSet = True
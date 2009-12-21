from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

class EnemyActor(Actor):
    def __init__(self):
        super(EnemyActor, self).__init__(0, 0, 0, 0)
        
        self.position = 0
    
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
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)

    def getPosition(self):
        block = self.board.path[self.position]
        
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * block.x, self.height * block.y)
    
    def getNextPosition(self):
        block = self.board.path[self.position + 1]
        
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * block.x, self.height * block.y)
    
    def start(self):
        (startX, startY) = self.getPosition()
        (nextX, nextY) = self.getNextPosition()
        anima = Animation(1000, self, "x", startX, nextX)
        animb = Animation(1000, self, "y", startY, nextY)
        self.addAnimation(anima)
        self.addAnimation(animb)
        anima.onCompletion(self.nextSquare)
        anima.start()
        animb.start()
    
    def nextSquare(self):
        self.position += 1
        self.start()
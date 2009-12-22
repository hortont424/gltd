from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

from Utilities import *

class EnemyActor(Actor):
    def __init__(self):
        super(EnemyActor, self).__init__(0, 0, 0, 0)
        
        self.position = 0
        self.hitPoints = 1000
        self.speed = 1000
    
    def render(self):
        abstract()
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)

    def getPosition(self):
        block = self.board.path[self.position]
        
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * block.x + (self.width / 2), self.height * block.y + (self.height / 2))
    
    def getNextPosition(self):
        block = self.board.path[self.position + 1]
        
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * block.x + (self.width / 2), self.height * block.y + (self.height / 2))
    
    def start(self):
        (startX, startY) = self.getPosition()
        (nextX, nextY) = self.getNextPosition()
        anim = Animation(self.speed, [("x", startX, nextX), ("y", startY, nextY)], IN_OUT_QUAD)
        self.addAnimation(anim)
        anim.onCompletion(self.nextSquare)
        anim.start()
    
    def nextSquare(self):
        self.position += 1
        self.start()
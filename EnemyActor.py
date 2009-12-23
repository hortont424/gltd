from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight
from ParticleActor import *

from Utilities import *

class EnemyActor(Actor):
    def __init__(self, hp):
        super(EnemyActor, self).__init__(0, 0, 0, 0)
        
        self.position = 0
        self.hitPoints = hp
        self.health = self.hitPoints
        self.speed = 1000
        self.baseColor = [1.0, 1.0, 1.0]
    
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
    
    def damage(self, d):
        self.health -= d
        self.opacity = min(float(self.health) / float(self.hitPoints) + 0.2, 1.0)
        
        if self.health <= 0:
            particles = ParticleActor(self.x, self.y, 50, 6.0)
            particles.color = self.baseColor
            self.window.addActor(particles)
            self.parent.removeEnemy(self)
        
        self.invalidate()
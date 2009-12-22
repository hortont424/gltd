from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

from Utilities import *

class TowerActor(Actor):
    def __init__(self, gridX, gridY):
        super(TowerActor, self).__init__(0, 0, 0, 0)
        
        self.gridX = gridX
        self.gridY = gridY
        self.damage = 500
        self.reloadSpeed = 1000
        self.range = 50
        self.targetEnemy = None
        
        self.weaponAngle = 0.0
    
    def render(self):
        abstract()
    
    def draw(self):
        (self.x, self.y) = self.getPosition()
        self.validate()
        glCallList(self.displayList)

    def getPosition(self):
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * self.gridX + (self.width / 2), self.height * self.gridY + (self.height / 2))
    
    def start(self):
        self.retarget()
    
    def retarget(self):
        self.weaponAngle = 90 + degrees(atan2(self.y - self.targetEnemy.y, self.x - self.targetEnemy.x))
        self.invalidate()
        anim = Animation(10, [], LINEAR)
        anim.onCompletion(self.retarget)
        self.addAnimation(anim)
        anim.start()
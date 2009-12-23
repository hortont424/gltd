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
        self.damage = 250
        self.reloadSpeed = 1000
        self.range = 50
        self.targetEnemy = None
        
        self.weaponAngle = 0.0
        self.fireTime = 0
    
    def render(self):
        self.rangeDisplayList = glGenLists(1)
        glNewList(self.rangeDisplayList, GL_COMPILE)
        glPushMatrix()
        
        glLineWidth(2)
        glColor4f(1.0, 1.0, 1.0, 0.1)
        
        glBegin(GL_LINE_STRIP)
        drawCircle(0.0, 0.0, self.range)
        glEnd()
        
        glPopMatrix()
        glEndList()
    
    def draw(self):
        (self.x, self.y) = self.getPosition()
        self.validate()
        glCallList(self.displayList)
        glCallList(self.rangeDisplayList)

    def getPosition(self):
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * self.gridX + (self.width / 2), self.height * self.gridY + (self.height / 2))
    
    def start(self):
        (self.x, self.y) = self.getPosition()
        self.retarget()
    
    def retarget(self):
        anim = Animation(50, [], LINEAR)
        anim.onCompletion(self.retarget)
        self.addAnimation(anim)
        anim.start()
        
        if self.distanceToEnemy() > self.range:
            return
        
        self.weaponAngle = 90 + degrees(atan2(self.y - self.targetEnemy.y, self.x - self.targetEnemy.x))
        self.invalidate()
        
        self.fire()
    
    def fire(self):
        abstract()
    
    def distanceToEnemy(self):
        # TODO: awkward to use width
        return sqrt((self.x - self.targetEnemy.x)**2 + (self.y - self.targetEnemy.y)**2) - (self.targetEnemy.width / 2)
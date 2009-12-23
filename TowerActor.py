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
        self.reloadSpeed = 700
        self.range = 50
        self.targetEnemy = None
        self.shake = 20
        
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

    def removeFromParent(self):
        self.parent.removeTower(self)

    def getPosition(self):
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)
        
        return (self.width * self.gridX + (self.width / 2), self.height * self.gridY + (self.height / 2))
    
    def start(self):
        (self.x, self.y) = self.getPosition()
        self.retarget(0)
    
    def retarget(self, timer):
        glutTimerFunc(50, self.retarget, 0)
        
        # Enemy is dead!
        if self.targetEnemy and self.targetEnemy.health <= 0:
            self.targetEnemy = None
        
        # Enemy is out of range!
        if self.targetEnemy and self.distanceToEnemy() > self.range:
            self.targetEnemy = None
        
        if not self.targetEnemy:
            targetEnemies = [(t.position, t) for t in self.window.enemies if self.distanceToGivenEnemy(t) < self.range]
            targetEnemies.sort()
            
            if len(targetEnemies):
                # Pick the enemy farthest along
                (position, enemy) = targetEnemies[-1]
                self.targetEnemy = enemy
            else:
                return
        
        if (not self.targetEnemy) or self.distanceToEnemy() > self.range:
            return
        
        self.weaponAngle = 90 + degrees(atan2(self.y - self.targetEnemy.y, self.x - self.targetEnemy.x))
        self.invalidate()
        
        self.fire()
    
    def fire(self):
        abstract()
    
    def distanceToGivenEnemy(self, enemy):
        # TODO: awkward to use width
        return sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2) - (enemy.width / 2)
    
    def distanceToEnemy(self):
        return self.distanceToGivenEnemy(self.targetEnemy)
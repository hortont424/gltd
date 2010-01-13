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
        
        self.active = True
        self.pickerTower = False
    
    def renderRange(self):
        if hasattr(self, "renderedRange"):
            glDeleteLists(self.rangeDisplayList, 1)
        
        self.renderedRange = self.range
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
    
    def render(self):
        # If we haven't created the display list for the range circle, or
        # the range has changed since the last time, render it!
        if self.active:
            if hasattr(self, "renderedRange"):
                if self.renderedRange != self.range:
                    self.renderRange()
            else:
                self.renderRange()
    
    def draw(self):
        # If inactive, allow position to be overridden
        self.updateSize()
        
        if self.active:
            (self.x, self.y) = self.getPosition()
        
        self.validate()
        glCallList(self.displayList)
        
        if self.active:
            glCallList(self.rangeDisplayList)

    def removeFromParent(self):
        self.parent.removeTower(self)

    def updateSize(self):
        self.width = (self.board.width / gridWidth)
        self.height = (self.board.height / gridHeight)

    def getPosition(self):
        return (self.width * self.gridX + (self.width / 2), self.height * self.gridY + (self.height / 2))
    
    def setPositionFromPixels(self, x, y):
        self.gridX = int((2*x)-self.width)/(2*self.width)
        self.gridY = int((2*y)-self.height)/(2*self.height)
    
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
                # Pick the enemy farthest along (this will need to be switchable)
                (position, enemy) = targetEnemies[-1]
                self.targetEnemy = enemy
            else:
                return
        
        if (not self.targetEnemy) or self.distanceToEnemy() > self.range:
            return
        
        angle = 90 + degrees(atan2(self.y - self.targetEnemy.y, self.x - self.targetEnemy.x))
        
        if abs(angle - self.weaponAngle) > 2.0: 
            self.weaponAngle = angle
            self.invalidate()
        
        self.fire()
    
    def fire(self):
        abstract()
    
    def distanceToGivenEnemy(self, enemy):
        # TODO: awkward to use width
        return sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2) - (enemy.width / 2)
    
    def distanceToEnemy(self):
        return self.distanceToGivenEnemy(self.targetEnemy)
    
    def mouseDown(self, button, x, y):
        # TODO: bring up menu if this is an active tower
        if self.active:
            return
        else:
            tower = self.__class__(0, 0)
            tower.active = False
            tower.pickerTower = True
            tower.x, tower.y = x, y
            self.window.addTower(tower)
            self.window.mouseActor = tower # TODO: THIS IS DISGUSTING

    def mouseUp(self, button, x, y):
        if self.pickerTower:
            self.active = True
            self.pickerTower = False
            self.setPositionFromPixels(x, y)
            self.window.addTower(self)
            self.start()
            self.invalidate()

    def mouseDrag(self, x, y):
        if self.pickerTower:
            self.x, self.y = x, y
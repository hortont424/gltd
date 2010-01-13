from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import *

from TowerActor import *
from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight
from EnemyActor import *
from ParticleActor import *

class RedL1BulletActor(Actor):
    def __init__(self, x, y, angle, velocity, damage):
        super(RedL1BulletActor, self).__init__(x, y, 5, 5)
        self.damage = damage
        nextX = x + cos(radians(angle)) * 800 # TODO: HACKY
        nextY = y + sin(radians(angle)) * 800
        anim = Animation(velocity, [("x", x, nextX), ("y", y, nextY)], LINEAR)
        anim.onFrame(self.collisionCheck)
        self.addAnimation(anim)
        anim.start()
    
    def draw(self):
        glPointSize(5)
        glBegin(GL_POINTS)
        glColor4f(0.8, 0.2, 0.4, 1.0)
        glVertex2f(0.0, 0.0)
        glEnd()
    
    def collisionCheck(self):
        if (self.x < self.board.x or self.x > self.board.width or
            self.y < self.board.y or self.y > self.board.height):
            self.window.removeActor(self)
        collisions = [self.window.pickingNames[c[0]] for c in self.window.pick(self.x, self.y) if isinstance(self.window.pickingNames[c[0]], EnemyActor)]
        
        if len(collisions):
            self.explode(collisions[0])
    
    def explode(self, enemy):
        self.window.addActor(ParticleActor(self.x, self.y))
        enemy.damage(self.damage)
        self.parent.removeActor(self)

class RedL1TowerActor(TowerActor):
    def __init__(self, gridX, gridY):
        super(RedL1TowerActor, self).__init__(gridX, gridY)
    
    def fire(self):
        if not self.active:
            return
        
        currentTime = glutGet(GLUT_ELAPSED_TIME)
        
        if self.distanceToEnemy() < self.range and currentTime - self.fireTime > self.reloadSpeed:
            if self.targetEnemy and self.targetEnemy.health > 0:
                self.fireTime = currentTime
                angle = self.weaponAngle + 90 + (choice([-1,1])*random()*self.shake)
                bullet = RedL1BulletActor(self.x, self.y, angle, 3500, self.damage)
                self.window.addActor(bullet)
    
    def render(self):
        super(RedL1TowerActor, self).render()
        
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        # Draw outer rectangle
        glBegin(GL_QUADS)
        size = self.width - 10
        glColor4f(0.8, 0.2, 0.4, 0.9)
        drawRect(- size / 2, - size / 2, size, size, 3)
        glEnd()
        
        glPointSize(7)
        glBegin(GL_POINTS)
        glColor4f(0.8, 0.2, 0.4, 1.0)
        glVertex2f(-size/2,-size/2)
        glVertex2f(-size/2,size/2)
        glVertex2f(size/2,-size/2)
        glVertex2f(size/2,size/2)
        glEnd()
        
        # Draw rotated segment for launcher
        glRotatef(self.weaponAngle, 0.0, 0.0, 1.0)
        
        # Draw inner rectangle
        
        glBegin(GL_QUADS)
        size = self.width - 24
        glColor4f(1.0, 1.0, 1.0, 0.2)
        drawRect(- size / 6, - size / 2, size / 3, size, 4)
        glColor4f(0.8, 0.2, 0.4, 1.0)
        drawRect(- size / 6, - size / 2, size / 3, size, 2)
        glEnd()
        
        glPopMatrix()
        
        glEndList()
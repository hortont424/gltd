from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from TowerActor import *
from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

class RedL1TowerActor(TowerActor):
    def __init__(self, gridX, gridY):
        super(RedL1TowerActor, self).__init__(gridX, gridY)
        
        #anim = Animation(5000, [("rotation", 0, 360)], LINEAR)
        #anim.loop = True
        #self.addAnimation(anim)
        #anim.start()
        
        #anim = Animation(250, [("scale", .8, 1.2)], IN_OUT_QUAD)
        #anim.loop = True
        #anim.pingPong = True
        #self.addAnimation(anim)
        #anim.start()
    
    def render(self):
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
        glPushMatrix()
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
        
        glPopMatrix()
        
        glEndList()
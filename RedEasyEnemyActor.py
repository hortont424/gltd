from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from EnemyActor import *
from Animation import *
from Actor import *
from GridActor import gridWidth, gridHeight

class RedEasyEnemyActor(EnemyActor):
    def __init__(self):
        super(RedEasyEnemyActor, self).__init__()
        
        anim = Animation(5000, "rotation", 0, 360, LINEAR)
        anim.loop = True
        self.addAnimation(anim)
        anim.start()
        
        anim = Animation(250, "scale", .8, 1.2, IN_OUT_QUAD)
        anim.loop = True
        anim.pingPong = True
        self.addAnimation(anim)
        anim.start()
    
    def render(self):
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glColor4f(0.8, 0.2, 0.4, 0.9)
        
        glBegin(GL_QUADS)
        
        size = self.width - 20
        drawRect(- size / 2, - size / 2, size, size, 3)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
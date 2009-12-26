from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from GroupActor import *

import time

class Window(GroupActor):
    subactors = []
    towers = []
    enemies = []
    pickingNames = {}
    currentPickingName = 0
    
    def __init__(self):
        super(Window, self).__init__(0, 0, 800, 600)
        
        glutInit("")
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(20, 20)
        glutCreateWindow("GLTD")
        
        self.window = self
        self.reshape(800, 600)

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutTimerFunc(16, self.idle, 0)
        
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        
        glEnable(GL_BLEND)
        
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
        
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glEnable(GL_TEXTURE_2D)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        self.lastTime = glutGet(GLUT_ELAPSED_TIME)
    
    def addTower(self, t):
        self.addActor(t)
        self.towers.append(t)
    
    def removeTower(self, t):
        self.removeActor(t)
        self.towers.remove(t)
    
    def addEnemy(self, t):
        self.addActor(t)
        self.enemies.append(t)
    
    def removeEnemy(self, t):
        self.removeActor(t)
        self.enemies.remove(t)
    
    def registerActor(self, actor):
        self.subactors.append(actor)
        self.currentPickingName += 1
        self.pickingNames[actor] = self.currentPickingName
        self.pickingNames[self.currentPickingName] = actor
    
    def unregisterActor(self, actor):
        self.subactors.remove(actor)
        del self.pickingNames[self.pickingNames[actor]]
        del self.pickingNames[actor]
    
    def reshape(self, width, height):
        self.width = width
        self.height = height
        
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -800, 800)
        glMatrixMode(GL_MODELVIEW)
        
        self.invalidate()
    
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glInitNames()
        
        self.draw()
        
        glutSwapBuffers()
    
    def pick(self, x, y):
        # maye need to set bufefer
        glSelectBuffer(64)
        glRenderMode(GL_SELECT)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluPickMatrix(x, y, 2, 2, glGetIntegerv(GL_VIEWPORT))
        glOrtho(0, self.width, 0, self.height, -800, 800)
        glMatrixMode(GL_MODELVIEW)
        glInitNames()
        
        self.draw()
        
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glFlush()
        
        return [c.names for c in glRenderMode(GL_RENDER)]
    
    def idle(self, timer):
        timeStep = glutGet(GLUT_ELAPSED_TIME) - self.lastTime
        self.animate(timeStep)
        
        for actor in self.subactors:
            actor.animate(timeStep)
        
        self.lastTime = glutGet(GLUT_ELAPSED_TIME)
        
        glutPostRedisplay()
        glutTimerFunc(15, self.idle, 0)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from GroupActor import *

from Utilities import *

import time

class Window(GroupActor):
    def __init__(self):
        super(Window, self).__init__(0, 0, 800, 600)
        
        self.subactors = []
        self.towers = []
        self.enemies = []
        self.pickingNames = {}
        self.currentPickingName = 0
        self.mouseActor = None
        
        glutInit("")
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(20, 20)
        glutCreateWindow("GLTD")
        
        self.window = self
        self.reshape(800, 600)

        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.activeMotion)
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
        glDisable(GL_LIGHTING)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        self.lastTime = glutGet(GLUT_ELAPSED_TIME)
    
    def addTower(self, t):
        if t not in self.subactors:
            self.addActor(t)
        self.towers.append(t)
    
    def removeTower(self, t):
        if t in self.subactors:
            self.removeActor(t)
        self.towers.remove(t)
    
    def addEnemy(self, t):
        if t not in self.subactors:
            self.addActor(t)
        self.enemies.append(t)
    
    def removeEnemy(self, t):
        if t in self.subactors:
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
        
        return flatten([c.names for c in glRenderMode(GL_RENDER)])
    
    def idle(self, timer):
        timeStep = glutGet(GLUT_ELAPSED_TIME) - self.lastTime
        renderTime = glutGet(GLUT_ELAPSED_TIME)
        self.animate(timeStep)
        
        for actor in self.subactors:
            actor.animate(timeStep)
        
        self.lastTime = glutGet(GLUT_ELAPSED_TIME)
        renderTime = self.lastTime - renderTime
        
        glutPostRedisplay()
        glutTimerFunc(5, self.idle, 0) # TODO: this should be less retarded
    
    def mouse(self, button, state, x, y):
        self.mouseActor = self.pickingNames[self.pick(x, self.height - y)[-1]]
        if state == GLUT_DOWN:
            self.mouseActor.mouseDown(button, x, self.height - y)
        elif state == GLUT_UP:
            self.mouseActor.mouseUp(button, x, self.height - y)
            self.mouseActor = None
    
    def activeMotion(self, x, y):
        if self.mouseActor:
            self.mouseActor.mouseDrag(x, self.height - y)
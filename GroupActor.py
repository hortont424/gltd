from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

import Settings

class GroupActor(Actor):
    def __init__(self, x, y, w, h):
        super(GroupActor, self).__init__(x, y, w, h)
        self.actors = []
        self.timeTotals = {}
        self.timeCounts = {}
    
    def draw(self):
        startDrawing = glutGet(GLUT_ELAPSED_TIME)
        
        glPushMatrix()
        
        glTranslatef(self.x, self.y, 0.0)
        
        for actor in self.actors:
            start = glutGet(GLUT_ELAPSED_TIME)
            glPushName(self.window.pickingNames[actor])
            glPushMatrix()
            glTranslatef(actor.x, actor.y, 0.0)
            glRotatef(actor.rotation, 0.0, 0.0, 1.0)
            glScalef(actor.scale, actor.scale, 1.0)
            actor.draw()
            glPopMatrix()
            glPopName()
            
            if Settings.DEBUGGING:
                if actor.__class__.__name__ in self.timeTotals:
                    self.timeTotals[actor.__class__.__name__] += glutGet(GLUT_ELAPSED_TIME) - start
                    self.timeCounts[actor.__class__.__name__] += 1
                else:
                    self.timeTotals[actor.__class__.__name__] = glutGet(GLUT_ELAPSED_TIME) - start
                    self.timeCounts[actor.__class__.__name__] = 1

        if Settings.DEBUGGING:
            for k in sorted(self.timeTotals.keys()):
                print k, self.timeTotals[k], float(self.timeTotals[k]) / self.timeCounts[k]
        
            print
        
        if Settings.DEBUGGING:
            print "Total", glutGet(GLUT_ELAPSED_TIME) - startDrawing
        
        glPopMatrix()
    
    def invalidate(self):
        super(GroupActor, self).invalidate()

        for actor in self.actors:
            actor.invalidate()
    
    def addActor(self, actor):
        actor.parent = self
        actor.window = self.window
        actor.board = self.board
        
        self.actors.append(actor)
        self.window.registerActor(actor)
    
    def removeActor(self, actor):
        self.actors.remove(actor)
        self.window.unregisterActor(actor)
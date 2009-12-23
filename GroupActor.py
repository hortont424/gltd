from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

class GroupActor(Actor):
    actors = []
    
    def __init__(self, x, y, w, h):
        super(GroupActor, self).__init__(x, y, w, h)
    
    def draw(self):
        glPushMatrix()
        
        glTranslatef(self.x, self.y, 0.0)
        
        for actor in self.actors:
            glPushName(self.window.pickingNames[actor])
            glPushMatrix()
            glTranslatef(actor.x, actor.y, 0.0)
            glRotatef(actor.rotation, 0.0, 0.0, 1.0)
            glScalef(actor.scale, actor.scale, 1.0)
            actor.draw()
            glPopMatrix()
            glPopName()
        
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
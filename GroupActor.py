from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

class GroupActor(Actor):
    actors = []
    
    def __init__(self, x, y):
        super(GroupActor, self).__init__(x, y)
    
    def draw(self, rect):
        glPushMatrix()
        
        glTranslatef(self.x, self.y, 0.0)
        
        for actor in self.actors:
            glPushMatrix()
            glTranslatef(actor.x, actor.y, 0.0)
            actor.draw((self.x, self.y, self.width, self.height))
            glPopMatrix()
        
        glPopMatrix()
    
    def addActor(self, actor):
        actor.parent = self
        actor.window = self.window
        
        self.actors.append(actor)
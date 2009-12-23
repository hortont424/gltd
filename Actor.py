from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Utilities import *

class Actor(object):
    def __init__(self, x, y, w, h):
        super(Actor, self).__init__()
        
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        
        self.rotation = 0.0
        self.scale = 1.0
        self.opacity = 1.0
        
        self.parent = None
        self.window = None
        self.board = None
        
        self.valid = False
        
        self.animations = []
    
    def draw(self):
        abstract()
    
    def render(self):
        abstract()
    
    def invalidate(self):
        self.valid = False
        if hasattr(self, "displayList"):
            glDeleteLists(self.displayList, 1)
    
    def validate(self):
        if not self.valid:
            self.render()
            self.valid = True
    
    def updatePosition(self):
        pass
    
    def animate(self, frames):
        for anim in self.animations:
            anim.update(self, frames)
            
            if (not anim.running) and (anim.ran):
                self.animations.remove(anim)
        #if len(self.animations) != 0:
        #    self.invalidate()
    
    def addAnimation(self, anim):
        self.animations.append(anim)
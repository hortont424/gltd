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
    
    def validate(self):
        if not self.valid:
            self.render()
            self.valid = True
    
    def updatePosition(self):
        pass
    
    def animate(self, frames):
        for anim in self.animations:
            anim.update(frames)
        self.invalidate()
    
    def addAnimation(self, anim):
        self.animations.append(anim)
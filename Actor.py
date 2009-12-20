from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Utilities import *

class Actor(object):
    def __init__(self, x, y):
        super(Actor, self).__init__()
        
        self.x = x
        self.y = y
        
        self.parent = None
        self.window = None
        
        self.valid = False
    
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
    
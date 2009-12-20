from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Utilities import *

class Actor(object):
    def __init__(self, x, y):
        super(Actor, self).__init__()
        
        self.x = x
        self.y = y
    
    def draw(self, rect):
        abstract()
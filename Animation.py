from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Animation(object):
    def __init__(self, duration, object, property, fromVal, toVal, easeFunction=None):
        super(Animation, self).__init__()
        self.duration = duration
        self.object = object
        self.property = property
        self.fromVal = fromVal
        self.toVal = toVal
        self.easeFunction = easeFunction
        self.startTime = 0
        self.running = False
    
    def start(self):
        self.startTime = glutGet(GLUT_ELAPSED_TIME)
        self.running = True
    
    def update(self, step):
        if not self.running:
            return
        
        self.currentPosition = (float(glutGet(GLUT_ELAPSED_TIME)) - self.startTime) / self.duration
        
        if self.currentPosition > 1.0:
            self.running = False
            setattr(self.object, self.property, self.toVal)
        
        setattr(self.object, self.property, float(self.fromVal) + (self.currentPosition * (self.toVal - self.fromVal)))
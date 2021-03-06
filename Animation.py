from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

def OUT_EXPO(t, b, c, d):
        return b+c if (t==d) else c * (-2**(-10 * t/d) + 1) + b;
 
def LINEAR (t, b, c, d):
    return c*t/d + b

def IN_QUAD (t, b, c, d):
    t/=d
    return c*(t)*t + b

def OUT_QUAD (t, b, c, d):
    t/=d
    return -c *(t)*(t-2) + b

def IN_OUT_QUAD(t, b, c, d):
    t/=d/2
    if ((t) < 1): return c/2*t*t + b
    t-=1
    return -c/2 * ((t)*(t-2) - 1) + b

def OUT_IN_QUAD(t, b, c, d):
    if (t < d/2): 
        return self.OUT_QUAD (t*2, b, c/2, d)
    return self.IN_QUAD((t*2)-d, b+c/2, c/2)

def IN_CUBIC(t, b, c, d):
    t/=d
    return c*(t)*t*t + b

def OUT_CUBIC(t, b, c, d):
    t=t/d-1
    return c*((t)*t*t + 1) + b

def IN_OUT_CUBIC(t, b, c, d):
    t/=d/2
    if ((t) < 1):
         return c/2*t*t*t + b
    t-=2
    return c/2*((t)*t*t + 2) + b

def OUT_IN_CUBIC(t, b, c, d):
    if (t < d/2): return self.OUT_CUBIC (t*2, b, c/2, d)
    return self.IN_CUBIC((t*2)-d, b+c/2, c/2, d)

def IN_QUART(t, b, c, d):
    t/=d
    return c*(t)*t*t*t + b

def OUT_QUART(t, b, c, d):
    t=t/d-1
    return -c * ((t)*t*t*t - 1) + b

def IN_OUT_QUART(t, b, c, d):
    t/=d/2
    if (t < 1): 
        return c/2*t*t*t*t + b
    t-=2
    return -c/2 * ((t)*t*t*t - 2) + b

class Animation(object):
    def __init__(self, duration, properties, easeFunction=LINEAR, invalidateEachFrame=False):
        super(Animation, self).__init__()
        self.duration = duration
        self.properties = properties
        self.easeFunction = easeFunction
        self.completionFunction = None
        self.frameFunction = None
        self.startTime = 0
        self.running = False
        self.loop = False
        self.pingPong = False
        self.reverse = False
        self.ran = False
        self.invalidateEachFrame = invalidateEachFrame
    
    def start(self):
        self.startTime = glutGet(GLUT_ELAPSED_TIME)
        self.running = True
        self.ran = True
    
    def update(self, object, step):
        if not self.running:
            return
        
        currentTime = (float(glutGet(GLUT_ELAPSED_TIME)) - self.startTime)
        
        if (currentTime / self.duration) > 1.0:
            self.running = False
            
            for (prop, fromVal, toVal) in self.properties:
                setattr(object, prop, toVal)
            
            if self.completionFunction:
                self.completionFunction()
            
            if self.loop:
                if self.pingPong:
                    self.properties = [(prop, toVal, fromVal) for (prop, fromVal, toVal) in self.properties]
                
                self.start()
            
            return
        
        for (prop, fromVal, toVal) in self.properties:
            newVal = self.easeFunction(float(currentTime), float(fromVal), float(toVal - fromVal), float(self.duration))
            setattr(object, prop, newVal)
        
        if self.frameFunction:
            self.frameFunction()
        
        if self.invalidateEachFrame:
            object.invalidate()
    
    def onCompletion(self, func):
        self.completionFunction = func
    
    def onFrame(self, func):
        self.frameFunction = func
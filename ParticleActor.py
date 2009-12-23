from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import *
from math import *

from Actor import *
from Animation import *

import numpy

class MasterParticleClockActor(Actor):
    def __init__(self):
        super(MasterParticleClockActor, self).__init__(0, 0, 0, 0)
        
        self.subparticles = []
        self.timerStarted = False
    
    def registerParticles(self, p):
        self.subparticles.append(p)
    
    def unregisterParticles(self, p):
        self.subparticles.remove(p)
    
    def updateParticles(self, timer):
        for a in self.subparticles:
            a.updateParticles()
        
        glutTimerFunc(16, self.updateParticles, 0)
    
    def draw(self):
        if not self.timerStarted:
            self.updateParticles(0)
            self.timerStarted = True

masterParticleClock = MasterParticleClockActor()

def randomParticle(x, y, color):
    angle = uniform(0, 6.28)
    v = uniform(0.5,3)
    return [x, y, cos(angle) * v, sin(angle) * v, color[0], color[1], color[2], 1.0]

class ParticleActor(Actor):
    def __init__(self, x, y, lifetime=30.0, size=1.0):
        super(ParticleActor, self).__init__(0, 0, 0, 0)
        
        self.lifetime = lifetime
        self.size = size
        self.color = [1.0, 0.0, 0.0] ## We'll have to fix this later...
        self.particles = numpy.array([randomParticle(x, y, self.color) for i in range(0, 25)])
        
        masterParticleClock.registerParticles(self)
    
    def updateParticles(self):
        # Make sure there are particles still alive. If so, animate them.
        # Otherwise, get rid of this actor!
        if self.particles[0][7] > 0.0:
            for p in self.particles:
                p[0] += p[2] # increment x by dx
                p[1] += p[3] # increment y by dy
                p[2] *= 0.95
                p[3] *= 0.95
                p[7] -= uniform(0.01, 0.05)
        else:
            self.parent.removeActor(self)
            masterParticleClock.unregisterParticles(self)
    
    def render(self):
        pass
    
    def draw(self):
        glPushMatrix()
        
        glPointSize(self.size)
        
        arrays = numpy.hsplit(self.particles,(2,4))
        
        glVertexPointerf(arrays[0])
        glColorPointerf(arrays[-1])
        glEnableClientState(GL_COLOR_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glDrawArrays(GL_POINTS, 0, len(self.particles))
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

        glPopMatrix()
        
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from random import *
from math import *

from Actor import *
from Animation import *

def randomParticle(x, y):
    angle = uniform(0, 6.28)
    v = uniform(0.5,3)
    return (x, y, cos(angle) * v, sin(angle) * v, 0)

class ParticleActor(Actor):
    def __init__(self, x, y, lifetime=30.0, size=1.0):
        super(ParticleActor, self).__init__(0, 0, 0, 0)
        
        self.particles = [randomParticle(x, y) for i in range(0, 50)]
        self.lifetime = lifetime
        self.size = size
        
        anim = Animation(10, [], LINEAR)
        anim.onCompletion(self.updateParticles)
        anim.loop = True
        self.addAnimation(anim)
        anim.start()
    
    def updateParticles(self):
        # Make sure there are particles still alive. If so, animate them.
        # Otherwise, get rid of this actor!
        if sum([1 for (x, y, dx, dy, l) in self.particles if l < self.lifetime]):
            self.particles = [(x+dx, y+dy, dx, dy, l + uniform(0.8,1.2)) for (x, y, dx, dy, l) in self.particles]
        else:
            self.parent.removeActor(self)
    
    def render(self):
        pass
    
    def draw(self):
        glPushMatrix()
        
        for (x, y, dx, dy, l) in self.particles:
            life = 1 - (float(l) / self.lifetime)
            
            if life <= 0.0:
                continue
            
            glPointSize(self.size * life)
            glBegin(GL_POINTS)
            glColor4f(1.0, 0.0, 0.0, life)
            glVertex2f(x, y)
            glEnd()
        
        glPopMatrix()
        
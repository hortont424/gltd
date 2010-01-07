from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.arrays import vbo
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy
import Image

from Actor import *
from Utilities import *

gridWidth = 15
gridHeight = 15

class GridTheme(object):
    darkBackground = [0.0, 0.0, 0.0, 0.0]
    lightBackground = [0.0, 0.0, 0.0, 0.0]
    gridLines = [0.0, 0.0, 0.0, 0.0]

class GridActorThemes(object):
    green = GridTheme()
    green.darkBackground = [0.000, 0.384, 0.145, 1.0]
    green.lightBackground = [0.204, 0.643, 0.396, 1.0]
    green.gridLines = [0.447, 0.812, 0.624, 0.8]
    
    blue = GridTheme()
    blue.darkBackground = [0.000, 0.145, 0.384, 1.0]
    blue.lightBackground = [0.204, 0.396, 0.643, 1.0]
    blue.gridLines = [0.447, 0.624, 0.812, 0.8]
    
    gray = GridTheme()
    gray.darkBackground = [0.1, 0.1, 0.1, 1.0]
    gray.lightBackground = [0.4, 0.4, 0.4, 1.0]
    gray.gridLines = [0.6, 0.6, 0.6, 0.8]

class GridActor(Actor):
    def __init__(self, x, y, w, h):
        super(GridActor, self).__init__(x, y, w, h)
        self.theme = GridActorThemes().blue
    
    def render(self):
        (dark, light) = (self.theme.darkBackground, self.theme.lightBackground)
        
        self.texture = createTexture(self.width, self.height)
        
        data = [[0.0, 0.0] + dark,
                [self.width, 0.0] + dark,
                [self.width, self.height] + light,
                [0, self.height] + light]
        
        for i in range(0, gridWidth):
            x = (self.width / gridWidth) * i
            data.append([x, 0] + self.theme.gridLines)
            data.append([x, self.height] + self.theme.gridLines)
        
        for i in range(0, gridHeight):
            y = (self.height / gridHeight) * i
            data.append([0, y] + self.theme.gridLines)
            data.append([self.width, y] + self.theme.gridLines)
        
        self.vbo = vbo.VBO(numpy.array(data, 'f'))
        
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
        glLineWidth(0.1)
        
        self.vbo.bind()
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(2, GL_FLOAT, 24, self.vbo)
        glColorPointer(4, GL_FLOAT, 24, self.vbo + 8)
        glDrawArrays(GL_QUADS, 0, 4)
        glDrawArrays(GL_LINES, 4, (gridWidth + gridHeight) * 2)
        glDisableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        self.vbo.unbind()
        
        glCopyTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 0, 0, self.width, self.height, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glBindTexture(GL_TEXTURE_2D, 0)
    
    def draw(self):
        self.validate()
        
        glBindTexture(GL_TEXTURE_2D, self.texture)
        
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        
        glBegin(GL_QUADS)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(0.0, 0.0)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(0.0, self.height)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(self.width, self.height)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(self.width, 0.0)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

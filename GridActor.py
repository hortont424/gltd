from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.arrays import vbo
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy

from Actor import *

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
        
        vertex = compileShader(
        """
        varying vec4 vertex_color;
        void main() {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
            vertex_color = gl_Color;
        }""", GL_VERTEX_SHADER)
        
        fragment = compileShader("""
        varying vec4 vertex_color;
        void main() {
            gl_FragColor = vertex_color;
        }""",GL_FRAGMENT_SHADER)
        
        self.shader = compileProgram(vertex,fragment)
        
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
    
    def draw(self):
        self.validate()
        
        glUseProgram(self.shader)
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
        glUseProgram(0)

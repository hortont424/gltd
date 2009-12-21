from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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
        self.displayList = glGenLists(1)
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glBegin(GL_QUADS)
        glColor4fv(self.theme.darkBackground)
        glVertex2f(0.0, 0.0)
        glVertex2f(self.width, 0.0)
        glColor4fv(self.theme.lightBackground)
        glVertex2f(self.width, self.height)
        glVertex2f(0, self.height)
        glEnd()
        
        glLineWidth(0.1)
        glColor4fv(self.theme.gridLines)

        glBegin(GL_LINES)
        
        for i in range(0, gridWidth):
            x = (self.width / gridWidth) * i
            glVertex2f(x, 0)
            glVertex2f(x, self.height)

        for i in range(0, gridHeight):
            y = (self.height / gridHeight) * i
            glVertex2f(0, y)
            glVertex2f(self.width, y)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)
        
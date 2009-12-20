from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *

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
    blue.darkBackground = [0.000, 0.384, 0.145, 1.0]
    blue.lightBackground = [0.204, 0.643, 0.396, 1.0]
    blue.gridLines = [0.447, 0.812, 0.624, 0.8]

class GridActor(Actor):
    def __init__(self):
        super(GridActor, self).__init__(0, 0)
        self.gridWidth = 15
        self.gridHeight = 15
        self.theme = GridActorThemes().green
    
    def render(self):
        self.displayList = glGenLists(1)
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glBegin(GL_QUADS)
        glColor4fv(self.theme.darkBackground)
        glVertex2f(0.0, 0.0)
        glVertex2f(self.window.width, 0.0)
        glColor4fv(self.theme.lightBackground)
        glVertex2f(self.window.width, self.window.height)
        glVertex2f(0, self.window.height)
        glEnd()
        
        glLineWidth(0.1)
        glColor4fv(self.theme.gridLines)

        glBegin(GL_LINES)
        
        for i in range(0, self.gridWidth):
            x = (self.window.width / self.gridWidth) * i
            glVertex2f(x, 0)
            glVertex2f(x, self.window.height)

        for i in range(0, self.gridHeight):
            y = (self.window.height / self.gridHeight) * i
            glVertex2f(0, y)
            glVertex2f(self.window.width, y)
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)
        
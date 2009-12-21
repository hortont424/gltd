from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Actor import *
from GridActor import gridWidth, gridHeight

from Polygon import *
from Polygon.Utils import *

class BoardTheme(object):
    background = [0.0, 0.0, 0.0, 0.0]
    gridLines = [0.0, 0.0, 0.0, 0.0]

class BoardActorThemes(object):
    green = BoardTheme()
    green.background = [0.447, 0.812, 0.624, 0.8]
    green.gridLines = [0.0, 0.0, 0.0, 0.3]

class BoardPathSegment(object):
    def __init__(self, x, y):
        self.neighbors = []
        self.x = x
        self.y = y
    
    def addNeighbor(n):
        self.neighbors.append(n)

class BoardActor(Actor):
    def __init__(self, x, y, w, h):
        super(BoardActor, self).__init__(x, y, w, h)
        self.theme = BoardActorThemes().green
        
        self.blocks = [None] * 20
        
        self.blocks[0] = BoardPathSegment(0, 7)
        self.blocks[1] = BoardPathSegment(1, 7)
        self.blocks[2] = BoardPathSegment(2, 7)
        self.blocks[3] = BoardPathSegment(3, 7)
        self.blocks[4] = BoardPathSegment(3, 8)
        self.blocks[5] = BoardPathSegment(4, 8)
        self.blocks[6] = BoardPathSegment(5, 8)
        self.blocks[7] = BoardPathSegment(5, 7)
        self.blocks[8] = BoardPathSegment(5, 6)
        self.blocks[9] = BoardPathSegment(5, 5)
        self.blocks[10] = BoardPathSegment(6, 5)
        self.blocks[11] = BoardPathSegment(7, 5)
        self.blocks[12] = BoardPathSegment(8, 5)
        self.blocks[13] = BoardPathSegment(9, 5)
        self.blocks[14] = BoardPathSegment(9, 4)
        self.blocks[15] = BoardPathSegment(10, 4)
        self.blocks[16] = BoardPathSegment(11, 4)
        self.blocks[17] = BoardPathSegment(12, 4)
        self.blocks[18] = BoardPathSegment(13, 4)
        self.blocks[19] = BoardPathSegment(14, 4)
        
        self.path = self.blocks[0]
    
    def render(self):
        tileWidth = (self.width / gridWidth)
        tileHeight = (self.height / gridHeight)
        shift = 4
        
        pathpoly = Polygon()
        for block in self.blocks:
            x = tileWidth * block.x
            y = tileHeight * block.y
            p = Polygon(((x - shift, y - shift), (x + tileWidth + shift, y - shift), (x + tileWidth + shift, y + tileHeight + shift), (x - shift, y + tileHeight + shift)))
            pathpoly += p
        
        self.displayList = glGenLists(1)
        
        glNewList(self.displayList, GL_COMPILE)
        
        glPushMatrix()
        
        glColor4fv(self.theme.background)

        glBegin(GL_QUADS)
        
        for block in self.blocks:
            x = tileWidth * block.x
            y = tileHeight * block.y
            glVertex2f(float(x), float(y))
            glVertex2f(float(x + tileWidth), float(y))
            glVertex2f(float(x + tileWidth), float(y + tileHeight))
            glVertex2f(float(x), float(y + tileHeight))
        
        glEnd()
        
        glColor4fv(self.theme.gridLines)
        
        glBegin(GL_QUADS)
        
        plist = pointList(prunePoints(pathpoly))
        plist.append(plist[0]) # close on self
        for i in range(len(plist)):
            (x1, y1) = plist[i]
            if i + 1 < len(plist):
                (x2, y2) = plist[i + 1]
            else:
                (x2, y2) = plist[i]
            
            width = 1.0
            half = width / 2.0
            
            if(x1 == x2):
                if y2 > y1:
                    y1 += width
                    y2 -= width
                else:
                    y1 -= width
                    y2 += width
                glVertex2f(float(x1 + half), float(y1 + half))
                glVertex2f(float(x1 - half), float(y1 - half))
                glVertex2f(float(x2 - half), float(y2 - half))
                glVertex2f(float(x2 + half), float(y2 + half))
            elif(y1 == y2):
                if x2 > x1:
                    x1 -= width
                    x2 += width
                else:
                    x1 += width
                    x2 -= width
                glVertex2f(float(x1 + half), float(y1 + half))
                glVertex2f(float(x1 - half), float(y1 - half))
                glVertex2f(float(x2 - half), float(y2 - half))
                glVertex2f(float(x2 + half), float(y2 + half))
        
        glEnd()
        
        glPopMatrix()
        
        glEndList()
    
    def draw(self):
        self.validate()
        glCallList(self.displayList)

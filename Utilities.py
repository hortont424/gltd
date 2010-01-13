from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.images import *
from OpenGL.GL.images import *

from math import *

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

def drawCircle(x, y, rad):
    for r in range (0, 360):
        i = float(radians(r))
        glVertex2f(rad * cos(i) + x, rad * sin(i) + y)
    glVertex2f(rad * cos(0) + x, rad * sin(0) + y)

def drawLine(x1, y1, x2, y2, width):
    half = float(width) / 2.0
    if(x1 == x2):
        if y2 > y1:
            y1 += width
            y2 -= width
        else:
            y1 -= width
            y2 += width
        glVertex2f(float(x1 + half), float(y1 - half))
        glVertex2f(float(x1 - half), float(y1 - half))
        glVertex2f(float(x2 - half), float(y2 + half))
        glVertex2f(float(x2 + half), float(y2 + half))
    elif(y1 == y2):
        if x2 > x1:
            x1 -= width
            x2 += width
        else:
            x1 += width
            x2 -= width
        glVertex2f(float(x1 + half), float(y1 + half))
        glVertex2f(float(x1 + half), float(y1 - half))
        glVertex2f(float(x2 - half), float(y2 - half))
        glVertex2f(float(x2 - half), float(y2 + half))

def drawRect(x, y, w, h, t):
    drawLine(x, y, x, y + h, t)
    drawLine(x, y + h, x + w, y + h, t)
    drawLine(x + w, y, x + w, y + h, t)
    drawLine(x, y, x + w, y, t)

def createTexture(width, height):
    texture = glGenTextures(1)
    
    data = createTargetArray(GL_RGB, (width, height), GL_UNSIGNED_BYTE)
    glBindTexture(GL_TEXTURE_2D, texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texture

# from http://kogs-www.informatik.uni-hamburg.de/~meine/python_tricks
def flatten(x):
    """flatten(sequence) -> list

    Returns a single, flat list which contains all elements retrieved
    from the sequence and all recursively contained sub-sequences
    (iterables).

    Examples:
    >>> [1, 2, [3,4], (5,6)]
    [1, 2, [3, 4], (5, 6)]
    >>> flatten([[[1,2,3], (42,None)], [4,5], [6], 7, MyVector(8,9,10)])
    [1, 2, 3, 42, None, 4, 5, 6, 7, 8, 9, 10]"""

    result = []
    for el in x:
        #if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from GroupActor import *

class Window(GroupActor):
    def __init__(self):
        super(Window, self).__init__(0, 0)
        
        glutInit("")
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutInitWindowSize(600, 600)
        glutInitWindowPosition(20, 20)

        glutCreateWindow("GLTD")
        self.window = self
        self.reshape(600, 600)

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        
        #glDepthFunc(GL_LESS)
        #glEnable(GL_DEPTH_TEST)
        #glShadeModel(GL_SMOOTH)
        
        glEnable(GL_BLEND)

        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)

        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glEnable(GL_TEXTURE_2D)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    def reshape(self, width, height):
        self.width = width
        self.height = height
        
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -800, 800)
        glMatrixMode(GL_MODELVIEW)
    
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        self.draw((0, 0, self.width, self.height))
        
        glutSwapBuffers()
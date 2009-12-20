#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Window import *
from GridActor import *

def main():
    window = Window()
    window.addActor(GridActor(100, 100))
    window.addActor(GridActor(200, 100))
    window.addActor(GridActor(400, 400))
    glutMainLoop()

main()
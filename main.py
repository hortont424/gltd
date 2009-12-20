#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Window import *
from GridActor import *

def main():
    window = Window()
    window.addActor(GridActor())
    glutMainLoop()

main()
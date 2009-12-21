#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Window import *
from GridActor import *
from BoardActor import *
from EnemyActor import *
from Animation import *

def main():
    window = Window()
    window.addActor(GridActor(0, 0, 600, 600))
    window.board = BoardActor(0, 0, 600, 600)
    window.addActor(window.board)
    
    enemy = EnemyActor()
    
    window.addActor(enemy)
    
    enemy.start()
    
    glutMainLoop()

main()
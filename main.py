#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Window import *
from GridActor import *
from BoardActor import *
from RedEasyEnemyActor import *
from RedL1TowerActor import *
from Animation import *

# tower.targetEnemy = enemy

class GLTD(object):
    def __init__(self):
        super(GLTD, self).__init__()
        
        self.window = Window()
        self.window.addActor(GridActor(0, 0, 600, 600))
        self.window.board = BoardActor(0, 0, 600, 600)
        self.window.addActor(self.window.board)

        anim = Animation(1864, [], LINEAR)
        anim.onCompletion(self.createNewEnemy)
        anim.loop = True
        self.window.addAnimation(anim)
        anim.start()

        tower = RedL1TowerActor(4,7)
        self.window.addTower(tower)
        tower.start()
        
        tower = RedL1TowerActor(10,5)
        tower.range = 150
        self.window.addTower(tower)
        tower.start()

        glutMainLoop()
    
    def createNewEnemy(self):
        enemy = RedEasyEnemyActor()
        self.window.addEnemy(enemy)
        enemy.start()
        print "made new enemy"

td = GLTD()
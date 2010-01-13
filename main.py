#!/usr/bin/env python

import Settings
import OpenGL

OpenGL.ERROR_CHECKING = Settings.DEBUGGING

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Window import *
from GridActor import *
from BoardActor import *
from RedEasyEnemyActor import *
from RedL1TowerActor import *
from Animation import *
from ParticleActor import *
from TowerChooser import *

class GLTD(object):
    def __init__(self):
        super(GLTD, self).__init__()
        
        self.totalEnemies = 1
        
        self.window = Window()
        self.window.addActor(GridActor(0, 0, 600, 600))
        self.window.board = BoardActor(0, 0, 600, 600)
        self.window.addActor(self.window.board)
        
        self.window.addActor(masterParticleClock) # TODO: unmessify. IMPORTANT
        
        #anim = Animation(20, [], LINEAR)
        #self.px = 10.0
        #self.py = 10
        #anim.onCompletion(self.createNewParticles)
        #anim.loop = True
        #self.window.addAnimation(anim)
        #anim.start()

        anim = Animation(1864, [], LINEAR)
        #################anim.onCompletion(self.createNewEnemy)
        anim.loop = True
        self.window.addAnimation(anim)
        anim.start()
        
        #tower = RedL1TowerActor(4,7)
        #self.window.addTower(tower)
        #tower.start()
        #
        #tower = RedL1TowerActor(10,5)
        #tower.range = 150
        #tower.reloadSpeed = 300
        #tower.damage = 1000
        #tower.shake = 2
        #self.window.addTower(tower)
        #tower.start()
        
        towerChooser = TowerChooser(600, 300, 200, 300)
        self.window.addActor(towerChooser)
        
        tower = RedL1TowerActor(0, 0)
        tower.active = False
        tower.x = tower.y = -0.0
        towerChooser.addActor(tower)

        glutMainLoop()
    
    def createNewEnemy(self):
        enemy = RedEasyEnemyActor(self.totalEnemies * 100)
        self.window.addEnemy(enemy)
        enemy.start()
        self.totalEnemies += 1
    
    def createNewParticles(self):
        if self.py > 600:
            return
        
        self.window.addActor(ParticleActor(20*sin(self.px) + 30,self.py))
        self.px += 0.5
        self.py += 5

def main():
    td = GLTD()

main()
#cProfile.run('main()', 'tl.prof')
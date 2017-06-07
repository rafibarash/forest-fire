import random
import turtle
from tree import *

class Forest():
    def __init__(self):
        self.forestList = []

    def prompts(self):
        '''prompts for density, percentPine, and wetness, and returns values'''
        density = float(input('What percentage of grid cells are occupied by trees? (0.10-1): '))
        percentPine = float(input('What percentage of trees are pine? (0.00-1): '))
        wetness = float(input('How wet is the forest? (1-3),(1=dry,3=wet): '))
        return density,percentPine,wetness

    def initialize_forest_list(self,density,percentPine,wetness):
        '''Loop that adds trees to self.forestlist'''
        for i in range(40):
            for j in range(40):
                random_density = random.uniform(0.1,1)
                if random_density <= density:
                    random_pine = random.uniform(0.0,1)
                    if random_pine <= percentPine:
                        obj = Pine(False,wetness,j,i)
                        self.addTree(obj)
                    else:
                        obj = Oak(False,wetness,j,i)
                        self.addTree(obj)
                else:
                    self.addTree(None)

    def initial_tree_on_fire(self):
        '''Setting a random tree on fire'''
        newList = []
        count=0
        for obj in self.forestList:
            if obj is not None:
                newList += [count]
            count += 1
        number = random.randint(0,len(newList)-1)
        fire_index = newList[number]
        self.forestList[fire_index].changeBurning(True)

    def addTree(self,obj):
        '''adds Tree to Forest'''
        self.forestList += [obj]
        
    def removeTree(self,index):
        '''removes Tree from Forest'''
        self.forestList[index] = None
        
    def update(self):
        '''updates burning status of trees in forest'''
        oldBurningTrees = []
        newBurningTrees = []
        forestlist = self.getForestList()
        for i in range(len(forestlist)):
            obj = forestlist[i]
            if obj != None:
                if obj.burning is True:
                    oldBurningTrees += [i]
                else:                   
                    random_num = random.random()
                    if random_num < obj.probCatch:
                        if self.hasBurningNeighbor(obj) is True:
                            newBurningTrees += [i]
        for i in oldBurningTrees:
            forestlist[i] = None
        for i in newBurningTrees:
            obj = forestlist[i]
            obj.burning = True
        self.forestList = forestlist
        
    def getForestList(self):
        '''returns forest list'''
        return self.forestList
    
    def isBurning(self):
        '''returns True if a tree is burning in forest, false otherwise'''
        count=0
        for obj in self.forestList:
            if obj != None:
                if obj.burning is True:
                    count+=1
        if count > 0:
            return True
        else:
            return False
        
    def hasBurningNeighbor(self,obj):
        '''checks if any neighbors are burning'''
        for tree in self.forestList:
            if (tree != None) and (obj != None):
                if tree is obj:
                    pass
                elif ((tree.xpos-obj.xpos) in range(-1,2)) and ((tree.ypos-obj.ypos) in range(-1,2)):
                    if tree.burning is True:
                        return True
            
    def redraw(self):
        '''redraws graphic display'''
        turtle.clearstamps()
        turtle.tracer(0,0)
        for obj in self.forestList:
            if obj != None:
                obj.draw()
        turtle.update()

import random
import turtle

class Tree():
    def __init__(self,burning=False,wetness=1.0,xpos=0,ypos=0):
        self.burning = burning
        self.wetness = wetness
        self.xpos = xpos
        self.ypos = ypos
    def changeBurning(self,burning):
        self.burning = burning

class Oak(Tree):
    def __init__(self,burning=False,wetness=1.0,xpos=0,ypos=0):
        super().__init__(burning,wetness,xpos,ypos)
        self.probCatch = 0.45/wetness
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        '''stamps tree on screen'''
        t = turtle
        t.hideturtle()
        t.penup()
        t.setpos(self.xpos,self.ypos)
        if self.burning is False:
            t.color('green')
        else:
            t.color('red')
        t.shape('circle')
        t.shapesize(0.65)
        t.settiltangle(90)
        t.stamp()

class Pine(Tree):
    def __init__(self,burning=False,wetness=1.0,xpos=0,ypos=0):
        super().__init__(burning,wetness,xpos,ypos)
        self.probCatch = 0.95/wetness
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        '''stamps tree on screen'''
        t = turtle
        t.hideturtle()
        t.penup()
        t.setpos(self.xpos,self.ypos)
        if self.burning is False:
            t.color('green')
        else:
            t.color('red')
        t.shape('triangle')
        t.shapesize(0.65)
        t.settiltangle(90)
        t.stamp()

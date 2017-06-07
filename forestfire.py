from forest import *
from tree import *
import turtle

def main():
    t = turtle
    f = Forest()
    density,percentPine,wetness = f.prompts()
    f.initialize_forest_list(density,percentPine,wetness)
    f.initial_tree_on_fire()
    t.setworldcoordinates(0,0,40,40)
    f.redraw()
    done = False
    while not done:
        f.update()
        f.redraw()
        if f.isBurning() is False:
            done is True


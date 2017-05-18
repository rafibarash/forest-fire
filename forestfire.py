# Rafi Barash, baras015
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect
# of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none
# of it was obtained from any source other than material presented during
# the course.

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


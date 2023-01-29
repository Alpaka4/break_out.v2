import pygame
from config_2 import *
from brick import Brick
class BrickRow:
    def __init__(self):
        self.row=[]
        y=80
        color=RED
        
        for i in range(20):
            x=i*BRICK_WIDTH
            brick=Brick(x,y,color)
            self.row.append(brick)
    def update(self):
        pass

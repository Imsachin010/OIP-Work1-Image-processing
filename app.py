import pygame, sys
from pygame.locals import *
import numpy as np
from keras.model import load_model
import cv2


WHITE = (255, 255, 255)
BLACK = (0,0,0)
pygame.init()

IMAGESAVE =False
Boundaryinc = 5
Windowsizex = 640
Windowsizey = 480
PREDICT = True
MODEL = load_model("E:\Programs 2023\ML Projects\image processing\Model\my_model.h5")
Displaysurface = pygame.display.set_mode((640,480))
white_int = Displaysurface.map_rgb(WHITE)
pygame.display.set_caption("My project")

iswriting = False

number_xcord = []
number_ycord = []
inmg_cnt = 1


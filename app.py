import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2


WHITE = (255, 255, 255)
BLACK = (0,0,0)
pygame.init()

IMAGESAVE = False
Boundaryinc = 5
Windowsizex = 640
Windowsizey = 480
PREDICT = True
MODEL = load_model("E:\OIP23\Work1\image processing\Model\my_model.h5")
Displaysurface = pygame.display.set_mode((640,480))
white_int = Displaysurface.map_rgb(WHITE)
pygame.display.set_caption("My project")

iswriting = False

number_xcord = []
number_ycord = []
inmg_cnt = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEMOTION and iswriting:
            xcord,ycord =event.pos
            pygame.draw.circle(Displaysurface, WHITE, (xcord,ycord), 4,0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)
        
        if event.type == MOUSEBUTTONDOWN:
            iswriting=True
        
        if event.type == MOUSEBUTTONUP:
            iswriting = False
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)

            rect_min_x, rect_max_x = max(number_xcord[0]- Boundaryinc,0),min(Windowsizex, number_xcord[-1]+Boundaryinc)
            rect_min_Y, rect_max_Y = max(number_ycord[0]-Boundaryinc,0),min(Windowsizey, number_ycord[-1]+Boundaryinc)

            number_xcord = []
            number_ycord = []

            img_arr = np.array(pygame.PixelArray(Displaysurface))
            if IMAGESAVE:
                cv2.imwrite("image.png")
                inmg_cnt +=1
            
            if PREDICT:
                image = cv2.resize(img_arr,(28,28))
                image = np.pad(image, (10,10), 'constant', constant_values=0)
                image = cv2.resize(image, (28,28))/white_int
                label = str(LABELS[np.argmax(MODEL.predict(image.reshape(28,28,1)))]).title()
                pygame.draw.rect(Displaysurface, RED, (rect_min_x, rect_min_Y, rect_max_x,rect_min_Y, rect_max_Y-rect_min_Y), 3)
            
            if event.type == KEYDOWN:
                if event.unicode =='N':
                    Displaysurface.fill(BLACK)
                    
        pygame.display.update()
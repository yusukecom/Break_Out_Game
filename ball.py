# http://gamepro.blog.jp/python/pygame/blockout_ball
import pygame
from pygame.locals import*
import math
import sys
import pygame.mixer
SCREEN = Rect(0, 0, 400, 400)

class paddle(pygame.sprit.Sprit):
    def__init__(self,filename):
      pygame.sprite.Sprite.__init__(self,self.containers)
      self.image = pygame.image.load(filename).convert()
      self.rect = self.image.get_rect()
      self.rect.bottom = SCREEN.bottom - 20
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(SCREE)
class Ball(pygame.sprite.Sprite):
    speed = 5
    angle_left = 135
    angle_right = 45

    def __init__(self, filename, paddle, blocks):
       pygame.sprite.Sprite.__init__(self,self.containers)
       self.image = pygame.image.load(filename).convert()
       self.rect = self.image.get_rect()
       self.dx = self.py = 0
       self.paddle = paddle
       self. blocks = blocks
       self.update = self.start
       self.hit = 0

     def start(self):
         self.rect.centerx = self.paddle.rect.centerx
         self.rect.bottom = self.paddle.rect.top
         if pygame.mouse.get_pressed()[0] ==  1:
             self.dx = 0
             self.dy = -self.speed
             self.update = self.move

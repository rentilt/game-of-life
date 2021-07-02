import pygame
import sys
import numpy as np
import cv2


class Display(object):
    def __init__(self,W,H):
        pygame.init()
        self.size=W,H
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Game-of-Life")
        self.W, self.H = W,H

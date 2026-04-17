import pygame

class Player:
    
    def __init__(self, x, y, s, c, n):
        self.pos = [x, y]
        self.size = s
        self.color = c
        self.name = n

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
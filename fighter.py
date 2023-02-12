import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

     #მოძრაობა
    def move(self):
        gravity = 0
        speed = 10
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            dx = speed
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_w]:
            self.vel_y = -30

        self.vel_y += gravity
        dy += self.vel_y

        self.rect.x += dx
        self.rect.y += dy

        # if self.rect.left + dx < 0:
        #     dx = -self.rect.left



    #დახატვა
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
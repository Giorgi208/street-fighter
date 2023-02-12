import pygame

class Fighter():
    def __init__(self, x, y):
        self.jump = False
        self.attack = False
        self.attack_type = 0
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

     #მოძრაობა
    def move(self, screen_width, screen_height, screen):
        gravity = 2
        speed = 10
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            dx = speed
        if key[pygame.K_a]:
            dx = -speed
        if key[pygame.K_w] and self.jump == False:
            self.jump = True
            self.vel_y = -30
        if key[pygame.K_r] or key[pygame.K_t]:
            self.my_attack(screen)
            if key[pygame.K_r]:
                self.attack_type = 1
            if key[pygame.K_t]:
                self.attack_type = 2


        self.vel_y += gravity
        dy += self.vel_y


        #მარცხენა საზღვარი
        if self.rect.x + dx < 0:
            dx = 0 - self.rect.x
        #მარჯვენა საზღვარი
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        #დახტომის კოდი
        if self.rect.bottom + dy > screen_height - 110:
            dy = screen_height - 110 - self.rect.bottom
            self.jump = False

        self.rect.x += dx
        self.rect.y += dy

    #შეტევა
    def my_attack(self, surface):
        self.attack = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
    #დახატვა
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
import pygame
from fighter import Fighter
clock = pygame.time.Clock()
fps = 60
pygame.init()

screen_width = 1000
screen_height = 600

pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.jpg")

def draw_background():
    scaled_background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(scaled_background, (0, 0))


fighter1 = Fighter(200, 310)
fighter2 = Fighter(700, 310)


run = True
while run:
    clock.tick(fps)
    draw_background()

    fighter1.draw(screen)
    fighter2.draw(screen)

    fighter1.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
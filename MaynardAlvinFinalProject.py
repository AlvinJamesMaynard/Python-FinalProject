
import pygame

sw = 800
sh = 600


asteroidBig = pygame.image.load('GamePics/asteroidBig.png')
asteroidMedium = pygame.image.load('GamePics/asteroidMedium.png')
asteroidSmall = pygame.image.load('GamePics/asteroidSmall.png')
spaceship = pygame.image.load('GamePics/spaceship.png')
starbackground = pygame.image.load('GamePics/starbackground.png')

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()

gameover = False


def redrawGameWindow():
    win.blit(bg, (0,0))

    pygame.display.update()

run = True
while run:
    clock.tick(60)
    if not gameover:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
pygame.quit()
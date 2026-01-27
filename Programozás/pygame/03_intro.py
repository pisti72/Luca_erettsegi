# https://www.pygame.org/docs/tut/PygameIntro.html
import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [400, 300]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = 0
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed[0] * dt, speed[1] * dt)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
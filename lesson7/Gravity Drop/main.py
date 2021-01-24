import pygame
import time

from Ball import *
from FasterBall import *

gravity = 0.005
all_sprites = []      # Keep a list of all sprites in 

ball_image = pygame.image.load("images/ball.png")
# dog_image = pygame.image.load("dog.jpg")

ball1 = Ball(ball_image,(200,150), gravity)
ball2 = Ball(ball_image,(50, 150), gravity)

fasterBall1 = FasterBall(ball_image, (400, 150), gravity)
all_sprites.append(ball1)
all_sprites.append(ball2)
all_sprites.append(fasterBall1)

def main():
    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((1080, 1080))

    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(main_surface)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
import pygame
import time
from random import randrange

from Trooper import *

WINDOW_SIZE = 1200
gravity = 0.02
sprites = []
stormtrooper_length = 50

stormtrooper_image = pygame.image.load("images/stormtrooper.png")
stormtrooper_image = pygame.transform.scale(stormtrooper_image, (stormtrooper_length, stormtrooper_length))
empire = Trooper(stormtrooper_image,(randrange(WINDOW_SIZE), randrange(WINDOW_SIZE)), gravity)
sprites.append(empire)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

def increased_score(score, increment):
    return score + increment

def clicked_square(pos, mouse_pos, image_length):
    x_ok = False
    y_ok = False
    if mouse_pos[0] >= pos[0] - image_length / 2:
        if mouse_pos[0] <= pos[0] + image_length / 2:
            x_ok = True
    if mouse_pos[1] >= pos[1] - image_length / 2:
        if mouse_pos[1] <= pos[1] + image_length / 2:
            y_ok = True
    return y_ok and x_ok

def run():
    pygame.init() # makes it so I can use pygame mod
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    main_surface = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) # How large the window is
    global score
    score = 0
    game_over = False
    while True:
        event = pygame.event.poll()
        if game_over:
            for i in sprites:
                sprites.remove(i)
            game_over_text = font.render("GAME OVER!", False, WHITE)
#            main_surface.blit(game_over_text, (50, 50))
            font.render_to(main_surface, (50, 50), "GAME OVER", WHITE)
        if event.type == pygame.QUIT:
            break;
        for s in sprites:
            if s.get_pos()[0] >= WINDOW_SIZE:
                game_over = True
                print("GAME OVER!")

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in sprites if clicked_square(s.get_pos(), pos, stormtrooper_length)]
            for i in clicked_sprites:
    	        sprites.remove(i)
                empire = Trooper(stormtrooper_image,(randrange(WINDOW_SIZE), randrange(WINDOW_SIZE)), gravity)
                sprites.append(empire)
                empire2 = Trooper(stormtrooper_image,(randrange(WINDOW_SIZE), randrange(WINDOW_SIZE)), gravity)
                sprites.append(empire2)
                score = score + 1
                print(score)

        main_surface.fill((30, 40, 5))
        for sprite in sprites:
            sprite.update() # updates sprites
            sprite.draw(main_surface) # redraws sprites
    	pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    run()


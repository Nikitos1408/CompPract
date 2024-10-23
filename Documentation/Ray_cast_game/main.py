import pygame
from settings import *
from menu import *
from player import Player
import math
import sys
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_menu()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math. sin(player.angle)), 2)
    # for x,y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())
import pygame
from settings import *
import math
import sys


pygame.init()

# Установка размеров окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Меню игры')

# Инициализация шрифта
pygame.font.init()
font = pygame.font.Font(None, 74)  # Основной шрифт для заголовка
button_font = pygame.font.Font(None, 50)  # Шрифт для кнопок

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def draw_button(surface, text, font, color, rect, border_color):
    pygame.draw.rect(surface, border_color, rect, 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def show_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button.collidepoint(mouse_x, mouse_y):
                    print("Start Game clicked")
                    menu = False  # Начать игру
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        window.fill(WHITE)

        # Отрисовка заголовка меню
        draw_text(window, 'Меню игры', font, BLACK, WIDTH // 2 - 150, 100)

        # Определение кнопок меню
        start_button = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)
        quit_button = pygame.Rect(WIDTH // 2 - 100, 350, 200, 50)

        # Отрисовка кнопок меню
        draw_button(window, 'Начать игру', button_font, BLACK, start_button, BLACK)
        draw_button(window, 'Выйти', button_font, BLACK, quit_button, BLACK)

        pygame.display.update()

def main_game():
    # Основной игровой цикл
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
        window.fill(GRAY)
        draw_text(window, 'Игра началась!', font, BLACK, WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 50)
        pygame.display.update()
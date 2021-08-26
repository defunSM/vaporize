import pygame
import os

from enemy import Enemy, BlueUFO
from player import Player

WIDTH, HEIGHT = 1000, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN_NAME = "Game"
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

VEL = 5
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Backgrounds', 'purple.png')), (WIDTH, HEIGHT))
BG_MAIN_THEME_SOUND = os.path.join("Assets", "music", "Heroic Demise (New).ogg")

pygame.display.set_caption(WIN_NAME)
moving_sprites = pygame.sprite.Group()
player = Player()
ufo = BlueUFO(WIDTH/2, 50)
moving_sprites.add(ufo)
moving_sprites.add(player)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0, 0))
    moving_sprites.draw(WIN)
    moving_sprites.update(0.2)
    pygame.display.update()

def main():

    # sound mixer
    pygame.mixer.init()
    main_theme = pygame.mixer.Sound(file=BG_MAIN_THEME_SOUND)
    main_theme.play()

    # FPS for game
    clock = pygame.time.Clock()
    run: bool = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                player.pos_x += 1

        # Moving left or right
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_a]:
            player.pos_x -= VEL
        if keys_pressed[pygame.K_d]:
            player.pos_x += VEL
        if keys_pressed[pygame.K_s]:
            player.pos_y += VEL
        if keys_pressed[pygame.K_w]:
            player.pos_y -= VEL

        draw_window()
        player.animate()

    main_theme.stop()
    pygame.mixer.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
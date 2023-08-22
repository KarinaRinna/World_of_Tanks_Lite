import pygame
import random


display_width = 800
display_height = 600

game_layout_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('World of Tanks Lite')

Resources = pygame.image.load("resources/game_background.png")
pygame.display.set_icon(Resources)

# colors
wheat = (245, 222, 179)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

#geometry of tank
tnk_width = 40
tnk_height = 20

tur_width = 5
whl_width = 5

# font size
s_font = pygame.font.SysFont("Times New Roman", 25)
m_font = pygame.font.SysFont("Times New Roman", 50)
l_font = pygame.font.SysFont("Times New Roman", 85)
vs_font = pygame.font.SysFont("Times New Roman", 25)

# score
def Score(Score):
    text = s_font.render("Score: " + str(Score), True, white)
    game_layout_display.blit(text, [0, 0])

# player tank
def tank(x, y, turret_position):
    x = int(x)
    y = int(y)

    pos_Turrets = [(x - 27, y - 2),
                   (x - 26, y - 5),
                   (x - 25, y - 8),
                   (x - 23, y - 12),
                   (x - 20, y - 14),
                   (x - 18, y - 15),
                   (x - 15, y - 17),
                   (x - 13, y - 19),
                   (x - 11, y - 21)
                   ]

    pygame.draw.circle(game_layout_display, blue, (x, y), int(tnk_height / 2))
    pygame.draw.rect(game_layout_display, blue, (x - tnk_height, y, tnk_width, tnk_height))

    pygame.draw.line(game_layout_display, blue, (x, y), pos_Turrets[turret_position], tur_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 15, y + 20), whl_width)

    return pos_Turrets[turret_position]

# computer tank
def computer_tank(x, y, turret_position):
    x = int(x)
    y = int(y)

    pos_Turrets = [(x + 27, y - 2),
                   (x + 26, y - 5),
                   (x + 25, y - 8),
                   (x + 23, y - 12),
                   (x + 20, y - 14),
                   (x + 18, y - 15),
                   (x + 15, y - 17),
                   (x + 13, y - 19),
                   (x + 11, y - 21)
                   ]

    pygame.draw.circle(game_layout_display, blue, (x, y), int(tnk_height / 2))
    pygame.draw.rect(game_layout_display, blue, (x - tnk_height, y, tnk_width, tnk_height))

    pygame.draw.line(game_layout_display, blue, (x, y), pos_Turrets[turret_position], tur_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 15, y + 20), whl_width)

    return pos_Turrets[turret_position]

# game control
def game_ctrls():
    gameControl = True

    while gameControl:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_layout_display.fill(black)
        msg_screen("Controls", white, -100, size="large")
        msg_screen("Fire: Spacebar", wheat, -30)
        msg_screen("Move Turret: Up and Down arrows", wheat, 10)
        msg_screen("Move Tank: Left and Right arrows", wheat, 50)
        msg_screen("Press D to raise Power % AND Press A to lower Power % ", wheat, 140)
        msg_screen("Pause: P", wheat, 90)

        btn("Play", 150, 500, 100, 50, green, light_green, action="play")
        btn("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        btn("Quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)

# https://itsourcecode.com/free-projects/python-projects/tank-game-python-with-source-code/

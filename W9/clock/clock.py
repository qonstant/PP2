import pygame as pg
import datetime
# -----------------------------------------------------------------
pg.init()
# Initializing-----------------------------------------------------
WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pg.time.Clock()
# Screen ----------------------------------------------------------
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Clock')
# Colors ----------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Background -----------------------------------------------------
background = pg.transform.scale(pg.image.load('img/Main.jpeg'), (WIDTH, HEIGHT))

# Music ----------------------------------------------------------
pg.mixer.music.load('./music/sound.mp3')
pg.mixer.music.play(-1)  # Reproduces sound endlessly
# Font ----------------------------------------------------------
font = pg.font.SysFont("Times New Roman", 30)

# Images -------------------------------------------------------------
right = pg.image.load('./img/HourHand.png')
left = pg.image.load('./img/MinHand.png')
# Changing resolution
# 1400//1,75 = 800 and 1050//1,75 = 600 then 1450x1050 => 800x600
rhand = pg.transform.scale(pg.image.load('img/HourHand.png'), (right.get_width()//1.75, right.get_height()//1.75))
lhand = pg.transform.scale(pg.image.load('img/MInHand.png'), (left.get_width()//1.75, left.get_height()//1.75))

# Rotate functions ------------------------------------------------------


def blit_rotate_center(image, x0, y0, angel):  # topleft x0 and y0 coordinates of the image
    rotated_image = pg.transform.rotate(image, angel)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=(x0, y0)).center)
    screen.blit(rotated_image, new_rect)


running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    # Buttons --------------------------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Time -----------------------------------------------------------
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    # Background -----------------------------------------------------
    screen.blit(background, (0, 0))
    text = font.render(f'The time is now: {hour}:{minute}:{second}', True, BLUE)
    blit_rotate_center(rhand, WIDTH // 2 - rhand.get_width()//2, HEIGHT // 2 - rhand.get_height()//2,
                       (-6*minute) - 11)  # Error 11
    blit_rotate_center(lhand, WIDTH // 2 - lhand.get_width() // 2, HEIGHT // 2 - lhand.get_height() // 2,
                       (-6*second) - 3)  # Error 3
    screen.blit(text, (250, 550))

    pg.display.update()
pg.quit()
exit()

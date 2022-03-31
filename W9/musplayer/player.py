import pygame
import pygame as pg
from os import listdir
from os.path import isfile, join
# -----------------------------------------------------------------
pg.init()
# Initializing-----------------------------------------------------
WIDTH = 800
HEIGHT = 400
FPS = 30
index = 0
stopped = True
played = False
clock = pg.time.Clock()
# Screen ----------------------------------------------------------
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Music Player')
# Colors ----------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Background -----------------------------------------------------
background = pg.transform.scale(pg.image.load('./img/bckground.jpeg'), (WIDTH, HEIGHT))

# Font ----------------------------------------------------------
font = pg.font.SysFont("./font/Roboto-Bold.ttf", 30)
# Musics ---------------------------------------------------------
playlist = [('./musics/'+file) for file in listdir('./musics') if isfile(join('./musics', file))]
print(playlist)
# Functions ------------------------------------------------------


def play(index):
    global stopped
    global played
    stopped = False
    played = True
    pg.mixer.music.load(playlist[index])
    pygame.mixer.music.play(-1)


def stop():
    global stopped
    global played
    played = True
    stopped = True
    pg.mixer.music.pause()


def resume():
    global stopped
    global played
    played = True
    stopped = False
    pg.mixer.music.unpause()


def next():
    global index
    global played
    stop()
    index += 1
    played = False
    if index == len(playlist):
        index = 0
    play(index)


def previous():
    global index
    global played
    stop()
    played = False
    index -= 1
    if index == -1:
        index = len(playlist) - 1
    play(index)


running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    # Text --------------------------------------------------------------------
    text1 = font.render("Use these keys to control the music:", True, WHITE)
    text2 = font.render("'<--' -- previous     'SPACE' -- play/pause/resume     '-->' -- next", True, WHITE)
    current = font.render(f"Current music is: {playlist[index][9:-4]} ", True, WHITE)
    screen.blit(text1, (20, HEIGHT - 100))
    screen.blit(text2, (20, HEIGHT - 70))
    screen.blit(current, (20, HEIGHT - 30))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and stopped:
                if played:
                    resume()
                else:
                    play(index)
            elif event.key == pg.K_SPACE and not stopped:
                stop()
            elif event.key == pg.K_LEFT:
                previous()
            elif event.key == pg.K_RIGHT:
                next()
    pg.display.flip()
pg.quit()
exit()

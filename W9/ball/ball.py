import pygame as pg
pg.init()
# Initialization ----------------------
WIDTH = 800
HEIGHT = 600
FPS = 60
# Colors ------------------------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Screen ------------------------------
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Circle")
# Music -------------------------------
pg.mixer.music.load("./music/slayer.mp3")
pg.mixer.music.play(-1)
# Font --------------------------------

# Set ----------------------------------
running = True
# Clock -------------------------------
clock = pg.time.Clock()
# Coordinates -------------------------
x, y = WIDTH//2, HEIGHT//2
x_change = 0
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_UP and y > 25:
        #         y -= 20
        #     elif event.key == pg.K_DOWN and y < HEIGHT - 25:
        #         y += 20
        #     elif event.key == pg.K_RIGHT and WIDTH - 25 > x:
        #         x += 20
        #     elif event.key == pg.K_LEFT and x > 25:
        #         x -= 20
    keys = pg.key.get_pressed()
    if (keys[pg.K_a] or keys[pg.K_LEFT]) and x > 25:
        x -= 20
    if (keys[pg.K_d] or keys[pg.K_RIGHT]) and WIDTH - 25 > x:
        x += 20
    if (keys[pg.K_w] or keys[pg.K_UP]) and y > 25:
        y -= 20
    if (keys[pg.K_s] or keys[pg.K_DOWN]) and y < HEIGHT - 25:
        y += 20
    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), 25)
    pg.display.flip()
pg.quit()
exit()

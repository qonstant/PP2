import pygame as pg
import random
import time
from collections import namedtuple
from config import params
import psycopg2

playerName = input("Enter your name:\n")

pg.init()
# Fonts ----------------------------------------------------------------------------------------------------------------
font = pg.font.SysFont("./font/Roboto-Bold.ttf", 30, True)
bigfont = pg.font.SysFont("./font/Roboto-Bold.ttf", 50, True)

# Directions -----------------------------------------------------------------------------------------------------------
class Direction():
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'

# Getting Positions ----------------------------------------------------------------------------------------------------
Point = namedtuple('Point', 'x y')

# Colors ---------------------------------------------------------------------------------------------------------------
WHITE = (255, 255, 255)
GOLD = (255, 223, 0)
RED = (200, 0, 0)
GREEN1 = (0, 51, 0)
GREEN2 = (0, 102, 0)
GREEN3 = (0, 40, 0)
BLACK = (0, 0, 0)
GRASS = (102, 153, 0)
# Variables ------------------------------------------------------------------------------------------------------------
BLOCK_SIZE = 20
SPEED = 7
LEVEL = 0
SCORE = 0
scorePlayer = 0
levelPlayer = 0
running = True
game_over = False
names = []

# Functions ------------------------------------------------------------------------------------------------------------
def act(command):
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()


def get_level(name):
    global levelPlayer
    try:
        get = f'''
            SELECT level FROM players WHERE username = {name};
        '''
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(get)
        output = current.fetchone()
        current.close()
        config.commit()
        levelPlayer = output[0]
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()


def get_score(name):
    global scorePlayer
    try:
        get = f'''
            SELECT score FROM players WHERE username = {name};
        '''
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(get)
        output = current.fetchone()
        current.close()
        config.commit()
        scorePlayer = output[0]
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()


def add_user(name, level, score):
    commands = (
        f'''
            INSERT INTO players(username, level, score)
            VALUES('{name}', {level}, {score});
        '''
    )
    act(commands)


def upd_level(name, lvl):
    commands = (
        f"""
        UPDATE players SET level = {lvl} WHERE username = '{name}';
        """
        )
    act(commands)


def upd_score(name, sc):
    commands = (
        f"""
        UPDATE players SET score = {sc} WHERE username = '{name}';
        """
        )
    act(commands)

def get_names():
    global names
    command = (
        '''
        SELECT username FROM players ORDER BY score DESC;
        '''
    )
    try:
        config = psycopg2.connect(**params)
        current = config.cursor()
        current.execute(command)
        names = [i[0] for i in current.fetchall()]
        current.close()
        config.commit()
    except Exception as E:
        print(str(E))
    if config is not None:
        config.close()

# Main Class -----------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self, WIDTH=800, HEIGHT=600):
        # Initializing -------------------------------------------------------------------------------------------------
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Snake')

        # Starting positions, directions -------------------------------------------------------------------------------
        self.direction = Direction.RIGHT
        self.head = Point(self.WIDTH // 2, self.HEIGHT // 2)
        # The initial snake with a length of 3 with its body coordinates -----------------------------------------------
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.megafood_exists = False # Appearance of Megafood
        self.level = 0 # Level
        self.score = 0
        self.food = None
        self.megafood = None
        self.current = 0 # Current time
        self.start = 0 # Start time
        self.difference = 0 # difference between times
        self.counter = 10 # Time
        self.food_move()
    # Moving Food to random positions ----------------------------------------------------------------------------------
    def food_move(self):
        x = random.randint(0, (self.WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()

    # Moving Megafood to random positions ------------------------------------------------------------------------------
    def megafood_move(self):
        x = random.randint(0, (self.WIDTH - BLOCK_SIZE*2) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.HEIGHT - BLOCK_SIZE*2) // BLOCK_SIZE) * BLOCK_SIZE
        self.start = time.time()
        self.megafood = Point(x, y)
        if self.food in self.snake:
            self.megafood_move()

    # Snake Turns and the Exit Condition -------------------------------------------------------------------------------
    def play_step(self):
        # User Inputs From Keyboard ------------------------------------------------------------------------------------
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pg.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pg.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pg.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        # Move ---------------------------------------------------------------------------------------------------------
        self.move(self.direction)  # Update The Head
        self.snake.insert(0, self.head)

        # Check If Game Over -------------------------------------------------------------------------------------------
        if self.collision():
            global levelPlayer
            global scorePlayer
            global SCORE
            global LEVEL
            LEVEL = self.level
            SCORE = self.score
            global game_over
            game_over = True

        # Place New Food -----------------------------------------------------------------------------------------------
        if self.head == self.food:
            self.score += 1
            self.food_move()
            if self.score // 5 > self.level:
                global SPEED
                if random.randint(1, 2) == 1 and not self.megafood:
                    self.megafood_exists = True
                    self.megafood_move()
                SPEED += 3
                self.level = (SPEED-7)//3
        else:
            self.snake.pop()

        if self.head == self.megafood:
            self.score += 10
            self.megafood_exists = False

        # Update Interface ---------------------------------------------------------------------------------------------

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        # Hits Boundary ------------------------------------------------------------------------------------------------
        if self.head.x > self.WIDTH - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.HEIGHT - BLOCK_SIZE or self.head.y < 0:
            pg.display.flip()
            return True
        # Hits Itself --------------------------------------------------------------------------------------------------
        if self.head in self.snake[1:]:
            return True
        return False


    def update(self):
        self.display.fill(GRASS)
        # Drawing Skin of Snake as two different rectangles ------------------------------------------------------------
        for skin in self.snake:
            if skin == self.head:
                pg.draw.rect(self.display, GREEN3, pg.Rect(skin.x, skin.y, BLOCK_SIZE, BLOCK_SIZE))
            else:
                pg.draw.rect(self.display, GREEN1, pg.Rect(skin.x, skin.y, BLOCK_SIZE, BLOCK_SIZE))
                pg.draw.rect(self.display, GREEN2, pg.Rect(skin.x + 4, skin.y + 4, 12, 12))
        # Drawing food -------------------------------------------------------------------------------------------------
        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        # Drawing Megafood in case of it exists ------------------------------------------------------------------------
        if self.megafood_exists:
            pg.draw.rect(self.display, BLACK,
                         pg.Rect(self.megafood.x, self.megafood.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                         pg.Rect(self.megafood.x + 4, self.megafood.y + 4, 12, 12))
        # Updating Score and Level Text --------------------------------------------------------------------------------
        text1 = font.render(f"Score: {self.score}", True, WHITE)
        text2 = font.render(f"Level: {self.level}", True, WHITE)

        # Updating Timer -----------------------------------------------------------------------------------------------
        self.current = time.time()
        self.difference = abs(int(self.current - self.start - self.counter))
        if self.start + self.counter - self.current >= 0:
            text4 = font.render(str(self.difference), True, WHITE)

        # Blit Score and Level -----------------------------------------------------------------------------------------
        self.display.blit(text1, (10, 10))
        self.display.blit(text2, (10, 30))
        # Blit Timer if Megafood exists and Time is greater than 0 -----------------------------------------------------
        if self.megafood_exists and self.start + self.counter - self.current >= 0:
            self.display.blit(text4, (10, 50))
        else:
            self.megafood_exists = False
        # Blit Restart Text in case of loss ----------------------------------------------------------------------------
        if self.collision():
            text3 = bigfont.render(f"Press R to Restart", True, WHITE)
            self.display.blit(text3, (self.HEIGHT // 2 - 50, self.WIDTH // 2 - 140))
        pg.display.flip()

    # Snake Movement ---------------------------------------------------------------------------------------------------
    def move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = Point(x, y)


# Game Loop ------------------------------------------------------------------------------------------------------------
game = Game()
while running:
    # game_over
    start = game.play_step()
    if game_over == True:
        get_names()
        if playerName in names:
            if SCORE > scorePlayer:
                upd_score(playerName, SCORE)
            if LEVEL > int(levelPlayer):
                upd_level(playerName, LEVEL)
            print('Updating')
        else:
            get_level(playerName)
            get_score(playerName)
            add_user(playerName, LEVEL, SCORE)
            print('Creating')
        get_names()
        print('TOP')
        for i in range(len(names)):
            print(i + 1, names[i])
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                # Restart Conditions -----------------------------------------------------------------------------------
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        levelPlayer = 0
                        scorePlayer = 0
                        SCORE = 0
                        LEVEL = 0
                        SPEED = 7
                        game = Game()
                        game_over = False
pg.quit()
exit()

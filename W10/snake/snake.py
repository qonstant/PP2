import pygame as pg
import random
from collections import namedtuple

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
RED = (200, 0, 0)
GREEN1 = (0, 51, 0)
GREEN2 = (0, 102, 0)
BLACK = (0, 0, 0)
GRASS = (102, 153, 0)
# Variables ------------------------------------------------------------------------------------------------------------
BLOCK_SIZE = 20
SPEED = 7
running = True
game_over = False

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
        self.level = 0
        self.score = 0
        self.food = None
        self.food_move()
    # Moving Food to random positions ----------------------------------------------------------------------------------
    def food_move(self):
        x = random.randint(0, (self.WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()
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
            global game_over
            game_over = True

        # Place New Food -----------------------------------------------------------------------------------------------
        if self.head == self.food:
            self.score += 1
            self.food_move()
            if self.score//5 > self.level:
                global SPEED
                self.level = self.score//5
                SPEED += 3
        else:
            self.snake.pop()

        # Update Interface ---------------------------------------------------------------------------------------------

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        # Hits Boundary ------------------------------------------------------------------------------------------------
        if self.head.x > self.WIDTH - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.HEIGHT - BLOCK_SIZE or self.head.y < 0:
            pg.display.flip()
            return True
        # Hits Itself --------------------------------------------------------------------------------------------------
        global game_over
        if self.head in self.snake[1:]:
            # pg.display.flip()
            return True

        return False

    def update(self):
        self.display.fill(GRASS)

        for skin in self.snake:
            pg.draw.rect(self.display, GREEN1, pg.Rect(skin.x, skin.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, GREEN2, pg.Rect(skin.x + 4, skin.y + 4, 12, 12))

        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text1 = font.render(f"Score: {self.score}", True, WHITE)
        text2 = font.render(f"Level: {self.level}", True, WHITE)
        self.display.blit(text1, (10, 10))
        self.display.blit(text2, (10, 30))
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
    score = game.play_step()
    if game_over == True:
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                # Restart Conditions -----------------------------------------------------------------------------------
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        SPEED = 7
                        game = Game()
                        game_over = False

pg.quit()
exit()

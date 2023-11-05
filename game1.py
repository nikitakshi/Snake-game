import random
import os
import time

# Define constants
WIDTH, HEIGHT = 20, 10
SNAKE_CHAR = '■'
FOOD_CHAR = '●'
EMPTY_CHAR = ' '

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        tail = self.body[0]
        new_tail = (tail[0] - self.direction[0], tail[1] - self.direction[1])
        self.body.insert(0, new_tail)

    def check_collision(self):
        head = self.body[-1]
        return (
            head in self.body[:-1] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        )

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

    def respawn(self):
        self.position = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

# Game functions
def print_board(snake, food):
    os.system('clear' if os.name == 'posix' else 'cls')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == food.position:
                print(FOOD_CHAR, end=' ')
            elif (x, y) in snake.body:
                print(SNAKE_CHAR, end=' ')
            else:
                print(EMPTY_CHAR, end=' ')
        print()

def get_user_input():
    key = input("Enter direction (w/a/s/d to move, q to quit): ").lower()
    if key == 'w':
        return (0, -1)
    elif key == 's':
        return (0, 1)
    elif key == 'a':
        return (-1, 0)
    elif key == 'd':
        return (1, 0)
    elif key == 'q':
        return 'quit'
    else:
        return (0, 0)

# Main game loop
snake = Snake()
food = Food()
score = 0

while True:
    print_board(snake, food)
    print(f"Score: {score}")  # Display current score
    direction = get_user_input()

    if direction == 'quit':
        break

    if direction != (0, 0):
        snake.direction = direction

    snake.move()

    if snake.body[-1] == food.position:
        snake.grow()
        food.respawn()
        score += 10  # Increase score when food is consumed

    if snake.check_collision():
        print_board(snake, food)
        print(f"Game Over! Score: {score}")  # Display final score
        break

    time.sleep(0.1)
s

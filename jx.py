import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial position and size
snake_size = 20
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

# Snake movement variables
snake_dx = 0
snake_dy = 0
snake_speed = 10

# Food position
food_x = round(random.randrange(0, WIDTH - snake_size) / 20) * 20
food_y = round(random.randrange(0, HEIGHT - snake_size) / 20) * 20

clock = pygame.time.Clock()

# Initialize score
score = 0
font_style = pygame.font.SysFont(None, 30)

# Function to display score on the screen
def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, RED)
    window.blit(score_text, [10, 10])

# Function to display "Game Over" message
def game_over_message():
    game_over_text = font_style.render("Game Over! Press SPACE to play again", True, RED)
    window.blit(game_over_text, [WIDTH // 2 - 200, HEIGHT // 2 - 20])

# Reset game function
def reset_game():
    global snake_x, snake_y, snake_dx, snake_dy, score, game_over
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_dx = 0
    snake_dy = 0
    score = 0
    game_over = False

# Game loop
game_over = False
game_reset = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -snake_speed
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = snake_speed
                snake_dx = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if the snake hits the boundaries
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True

    # Check if the snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WIDTH - snake_size) / 20) * 20
        food_y = round(random.randrange(0, HEIGHT - snake_size) / 20) * 20
        score += 1

    # Clear the window
    window.fill(BLACK)

    # Draw the snake and the food
    pygame.draw.rect(window, GREEN, (food_x, food_y, snake_size, snake_size))
    pygame.draw.rect(window, RED, (snake_x, snake_y, snake_size, snake_size))

    # Display the score
    display_score(score)

    # Display game over message if the game is over
    if game_over:
        game_over_message()

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(30)

    # Check if the player wants to play again
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_over = False

# Quit the game
pygame.quit()

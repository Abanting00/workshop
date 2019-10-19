import pygame
from snake import Snake

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# created a new game
pygame.init()

# set screen size and screen display 
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set game title
pygame.display.set_caption("Snake Game")

# While we're not done with the game
done = False

# how fast a screen updates
clock = pygame.time.Clock()

# -------- Create a Snake -------------
length = 20
snake = Snake(length, BLACK)
snake_speed = snake.get_snake_speed()
x_speed = snake.speed
y_speed = 0

while not done:
	# tracks our keyboard and mouse input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("Left")
				x_speed = snake_speed *-1
				y_speed = 0

			# 5 mins activity: Check for right, down, and up keys
			if event.key == pygame.K_RIGHT:
				print("Right")
				x_speed = snake_speed
				y_speed = 0

			if event.key == pygame.K_DOWN:
				print("Down")
				x_speed = 0
				y_speed = snake_speed

			if event.key == pygame.K_UP:
				print("Up")
				x_speed = 0
				y_speed = snake_speed * -1

	# ---- Change our snake direction ---
	snake.change_direction(x_speed, y_speed)
	screen.fill(WHITE)

	# --- Draw Snake in our Screen -----
	snake.get_snake().draw(screen)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
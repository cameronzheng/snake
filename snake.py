import pygame

# 10x10 grid of snake

# pygame setup
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True



dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
  # poll for eventws 
  # pygame.QUIT event means teh user clicked X to close your window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER GAME HERE
    # border of the game
    top_left_point = [15, 15]
    top_right_point = [screen_width - 15, 15]
    bot_left_point = [15, screen_height - 15]
    bot_right_point = [screen_width - 15, screen_height - 15]

    pygame.draw.line(screen, "white", top_left_point, top_right_point, width = 2)  # top border
    pygame.draw.line(screen, "white", bot_left_point, bot_right_point, width = 2)  # bottom border
    pygame.draw.line(screen, "white", top_left_point, bot_left_point, width = 2)  # left border
    pygame.draw.line(screen, "white", top_right_point, bot_right_point, width = 2)  # right border
    
    # drawing the background for game
    for i in range(10):
      pygame.draw.rect(screen, "light green", (top_left_point[0], top_left_point[1] + 50 * i, screen_width - 30, 20))
      pygame.draw.rect(screen, "green", (top_left_point[0], top_left_point[1] + 20 + 50 * i, screen_width - 30, 20))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000

pygame.quit()
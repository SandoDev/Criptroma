import pygame

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("My Game")

background = 25, 25, 25
screen.fill(background)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(bg)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

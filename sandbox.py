import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Fade-In Effect")

# Load the image
image = pygame.image.load("images\mapa.png")

# Set the initial transparency of the image
image.set_alpha(0)

# Set the fade-in speed
fade_in_speed = 1

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Increase the transparency of the image
    image.set_alpha(image.get_alpha() + fade_in_speed)

    # Draw the image
    screen.blit(image, (0, 0))
    pygame.time.delay()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

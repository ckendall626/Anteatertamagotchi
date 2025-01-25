import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tamagotchi Task Manager")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white background
    screen.fill(WHITE)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()

pet_stats = {"hunger": 100, "happiness": 100, "energy": 100}

def update_pet_stats():
    pet_stats["hunger"] -= 1
    pet_stats["happiness"] -= 1
    pet_stats["energy"] -= 1

    # Prevent stats from going negative
    for stat in pet_stats:
        pet_stats[stat] = max(0, pet_stats[stat])

font = pygame.font.Font(None, 36)

def draw_stats():
    y_offset = 50
    for stat, value in pet_stats.items():
        text = font.render(f"{stat.capitalize()}: {value}", True, BLACK)
        screen.blit(text, (20, y_offset))
        y_offset += 40

pet_image = pygame.image.load("pet_happy.png")

def draw_pet():
    screen.blit(pet_image, (300, 200))
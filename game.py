import pygame
import sys
import pickle

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

#User Task handling
tasks = [{"name": "Finish homework", "completed": False},
         {"name": "Go for a walk", "completed": False}]

def draw_tasks():
    y_offset = 200
    for task in tasks:
        task_text = f"[{'X' if task['completed'] else ' '}] {task['name']}"
        text = font.render(task_text, True, BLACK)
        screen.blit(text, (20, y_offset))
        y_offset += 40

def complete_task(index):
    if not tasks[index]["completed"]:
        tasks[index]["completed"] = True
        pet_stats["happiness"] += 20
        pet_stats["energy"] += 10

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        complete_task(0)
    elif keys[pygame.K_2]:
        complete_task(1)

def save_progress():
    with open("progress.pkl", "wb") as f:
        pickle.dump({"tasks": tasks, "pet_stats": pet_stats}, f)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress()
            running = False

    # Fill screen with white background
    handle_input()
    update_pet_stats()

    screen.fill(WHITE)
    draw_stats()
    draw_tasks()
    draw_pet()
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()

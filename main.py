import json
import os
import random
import sys
import pygame
import factory
from shape import Rectangle, Circle, Triangle, Parallelogram


print("Hello World")
factory.register("rectangle", Rectangle)
factory.register("circle", Circle)
factory.register("triangle", Triangle)
factory.register("parallelogram", Parallelogram)

with open('./shapes.json') as file:
    data = json.load(file)

print(data)

shapes = [factory.create(item) for item in data["shapes"]]
positions = ["top_left", "top_right", "bottom_left", "bottom_right"]

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption("Shapes Game")

print(f"Screen Width: {SCREEN_WIDTH}")
print(f"Screen Height: {SCREEN_HEIGHT}")

SCREEN_WIDTH_MARGIN = int((SCREEN_WIDTH / 100 * 5) / 2)
SCREEN_HEIGHT_MARGIN = int((SCREEN_HEIGHT / 100 * 5) / 2)

print(f"Screen Width Margin: {SCREEN_WIDTH_MARGIN}")
print(f"Screen Height Margin: {SCREEN_HEIGHT_MARGIN}")

SCREEN_INNER_WIDTH = SCREEN_WIDTH - (SCREEN_WIDTH_MARGIN * 2)
SCREEN_INNER_HEIGHT = SCREEN_HEIGHT - (SCREEN_HEIGHT_MARGIN * 2)

print(f"Screen Inner Width: {SCREEN_INNER_WIDTH}")
print(f"Screen Inner Height: {SCREEN_INNER_HEIGHT}")

GRID_SIZE_WIDTH = int(SCREEN_INNER_WIDTH / 2)
GRID_SIZE_HEIGHT = int(SCREEN_INNER_HEIGHT / 2)

print(f"Screen Grid Width: {GRID_SIZE_WIDTH}")
print(f"Screen Grid Height: {GRID_SIZE_HEIGHT}")


def drawGrid():
    title = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 20, 760, 96))
    top_left_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 136, 370, 212))
    top_right_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (410, 136, 370, 212))
    bottom_left_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 368, 370, 212))
    bottom_right_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (410, 368, 370, 212))

    random.shuffle(shapes)
    for index, shape in enumerate(shapes):
        print(shape, end="\n")
        print(shape.draw(positions[index]))

        shape_parameters = shape.draw(positions[index])
        if shape.method == 'rect':
            pygame.draw.rect(SCREEN, shape_parameters[0], shape_parameters[1])
        elif shape.method == 'circle':
            pygame.draw.circle(SCREEN, shape_parameters[0], shape_parameters[1], shape_parameters[2])
        elif shape.method == 'polygon':
            pygame.draw.polygon(SCREEN, shape_parameters[0], shape_parameters[1])


while True:
    drawGrid()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


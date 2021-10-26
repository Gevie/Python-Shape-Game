import json
import os
import random
import sys
import pygame
import factory
from shape import Rectangle, Circle, Triangle, Parallelogram

os.environ["SDL_VIDEO_CENTERED"] = "1"


def load_shapes():
    factory.register("rectangle", Rectangle)
    factory.register("circle", Circle)
    factory.register("triangle", Triangle)
    factory.register("parallelogram", Parallelogram)

    with open('./shapes.json') as file:
        data = json.load(file)

    return [factory.create(item) for item in data["shapes"]]


def draw():
    title = pygame.draw.rect(SCREEN, (0, 0, 0), (20, 20, 760, 96))
    clear_drawings = pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))

    random.shuffle(shapes)
    for index, shape in enumerate(shapes):
        position = shape.map(positions[index])

        # TODO: Fix the issue with pygame and being able to draw the shape from the shape class
        # TODO: This is a dirty hack because of the 24 hour deadline from start to finish
        if shape.method == 'rect':
            pygame.draw.rect(SCREEN, shape.colour, position)
        elif shape.method == 'circle':
            pygame.draw.circle(SCREEN, shape.colour, position, shape.radius)
        elif shape.method == 'polygon':
            pygame.draw.polygon(SCREEN, shape.colour, position)


shapes = load_shapes()
positions = ["top_left", "top_right", "bottom_left", "bottom_right"]

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# TODO: Build structure / classes to handle events better
generate_new_round = pygame.USEREVENT + 1
pygame.time.set_timer(generate_new_round, 5000)

draw()
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == generate_new_round:
            draw()

    pygame.display.update()

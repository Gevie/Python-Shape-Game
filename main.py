import json
import os
import random
import sys
import pygame
import factory
import loader
from shape import Rectangle, Circle, Triangle, Parallelogram, Shape
from classes import ManageTimestamps
from PIL import Image
import glob
import time

os.environ["SDL_VIDEO_CENTERED"] = "1"

data_management = ManageTimestamps
data_management.initialize_test()

def load_shapes():
    """Load the shapes from the json file and use a factory to create instances"""

    factory.register("rectangle", Rectangle)
    factory.register("circle", Circle)
    factory.register("triangle", Triangle)
    factory.register("parallelogram", Parallelogram)

    with open('shapes.json') as file:
        data = json.load(file)
        loader.load_plugins(data["plugins"])

    return [factory.create(item) for item in data["shapes"]]


def draw_end_game():
    """Draw the end game screen"""
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))

    font = pygame.font.Font(None, 48)
    text = font.render("Thank you for your time.", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    SCREEN.blit(text, text_rect)


def draw() -> Shape:
    """Draw the next round screen and return the chosen shape"""
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))

    random.shuffle(shapes)
    for index, shape in enumerate(shapes):
        if index > 3:
            break

        position = shape.map(positions[index])

        # TODO: Fix the issue with pygame and being able to draw the shape from the shape class
        # TODO: This is a dirty hack because of the 24 hour deadline from start to finish
        if shape.method == 'rect':
            pygame.draw.rect(SCREEN, shape.colour, position)
        elif shape.method == 'circle':
            pygame.draw.circle(SCREEN, shape.colour, position, shape.radius)
        elif shape.method == 'polygon':
            pygame.draw.polygon(SCREEN, shape.colour, position)
        elif shape.method == 'line':
            pygame.draw.line(SCREEN, shape.colour, position[0], position[1], shape.radius)

    target_shape = shapes[random.randint(0, 3)]
    while target_shape.method == last_shape:
        target_shape = shapes[random.randint(0, 3)]

    font = pygame.font.Font(None, 48)
    text = font.render(f"{current_round}. Please select the {target_shape.type}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 50))
    SCREEN.blit(text, text_rect)

    return target_shape


def draw_second_stage() -> Shape:
    """Draw the next round screen and return the chosen shape"""
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))

    random.shuffle(shapes)
    for index, shape in enumerate(shapes):
        if index > 0:
            break

        position = shape.map(positions[index])

        # TODO: Fix the issue with pygame and being able to draw the shape from the shape class
        # TODO: This is a dirty hack because of the 24 hour deadline from start to finish
        if shape.method == 'rect':
            pygame.draw.rect(SCREEN, shape.colour, position)
        elif shape.method == 'circle':
            pygame.draw.circle(SCREEN, shape.colour, position, shape.radius)
        elif shape.method == 'polygon':
            pygame.draw.polygon(SCREEN, shape.colour, position)
        elif shape.method == 'line':
            pygame.draw.line(SCREEN, shape.colour, position[0], position[1], shape.radius)

    target_shape = shapes[random.randint(0, 3)]
    while target_shape.method == last_shape:
        target_shape = shapes[random.randint(0, 3)]

    font = pygame.font.Font(None, 48)
    text = font.render(f"{current_round}. Please select the {target_shape.type}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 50))
    SCREEN.blit(text, text_rect)

    return target_shape


def draw_third_stage() -> Shape:
    """Draw the next round screen and return the chosen shape"""
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))
    path = '*/IAPS/*.jpg'
    IAPS = []
    for filename in glob.glob(path):
        IAPS.append(filename)
    figure = random.choice.pop(IAPS) # TODO: figure out if this is correct use
    image = pygame.image.load(figure)
    SCREEN.fill(0, 0, 0)
    SCREEN.blit(image, (0, 0))
    return figure

# TODO: clear method
def draw_whitespace():
    """Draw the next round screen and return the chosen shape"""
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 800, 600))
    SCREEN.fill(255, 255, 255)


shapes = load_shapes()
positions = ["top_left", "top_right", "bottom_left", "bottom_right"]

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# TODO: Build structure / classes to handle events better
generate_new_round = pygame.USEREVENT + 1
pygame.time.set_timer(generate_new_round, 5000)

max_rounds = 81
current_round = 1
whitespace_rounds = [25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 61,
                     62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 77, 79, 80]
last_shape = None
winning_shape = draw()
clickable = True

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == generate_new_round and current_round <= 24:
            current_round = current_round + 1

            if current_round > 44:
                data_management.database_commit()
                draw_end_game()
            if current_round < 12:
                clickable = True
                winning_shape = draw()
                last_shape = winning_shape.type
                continue
            if 12 < current_round < 24:
                clickable = True
                winning_shape = draw_second_stage()
                last_shape = winning_shape.type
                continue

        if events.type == pygame.MOUSEBUTTONDOWN and current_round <= 24 and clickable is True:
            clicked = SCREEN.get_at(pygame.mouse.get_pos())
            if clicked == winning_shape.colour:
                clickable = False
                print(f"You clicked the {winning_shape.type} successfully.")
                if current_round == 1:
                    stage = 'Baseline'
                    data_management.create_timestamp(stage)

                else:
                    stage = f'Q{current_round}'
                    data_management.create_timestamp(stage)
        if 24 < current_round < 44:
            if current_round not in whitespace_rounds:
                file = draw_third_stage()
                stage = f'IAPS{current_round}'
                data_management.create_timestamp(stage)
                continue
            if current_round in whitespace_rounds:
                stage = 'Baseline'
                data_management.create_timestamp(stage)
                draw_whitespace()
                continue
    pygame.display.update()


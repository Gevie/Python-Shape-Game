import json
import os
import random
import sys
import pygame
import factory
import loader
from shape import Rectangle, Circle, Triangle, Parallelogram, Shape
from PIL import Image
import glob
from recording import SimpleRecording
from subject import Round
from subject import Instance
from subject import Subject
from datetime import date
import time

os.environ["SDL_VIDEO_CENTERED"] = "1"

path = './IAPS/*.jpg'

IAPS = []
for filename in glob.glob(path):
    IAPS.append(filename)


class Drawing:
    @staticmethod
    def clear_screen(colour: tuple = (0, 0, 0), width: int = 800, height: int = 600):
        pygame.draw.rect(SCREEN, colour, (0, 0, width, height))

    @staticmethod
    def draw_center_text(text: str):
        font = pygame.font.Font(None, 48)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        SCREEN.blit(text, text_rect)

    @staticmethod
    def draw_shape(shape: Shape, position):
        if shape.method == 'rect':
            pygame.draw.rect(SCREEN, shape.colour, position)
        elif shape.method == 'circle':
            pygame.draw.circle(SCREEN, shape.colour, position, shape.radius)
        elif shape.method == 'polygon':
            pygame.draw.polygon(SCREEN, shape.colour, position)

    def draw_image(self, image: Image):
        pass

    @staticmethod
    def draw_heading(text: str):
        font = pygame.font.Font(None, 48)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 50))
        SCREEN.blit(text, text_rect)


def load_shapes() -> list:
    """
    Load the shapes from the json file and use a factory to create instances

    Returns:
        list: A list of shape objects
    """

    factory.register("rectangle", Rectangle)
    factory.register("circle", Circle)
    factory.register("triangle", Triangle)
    factory.register("parallelogram", Parallelogram)

    with open('shapes.json') as file:
        data = json.load(file)
        loader.load_plugins(data["plugins"])

    return [factory.create(item) for item in data["shapes"]]


def draw_end_game(drawing: Drawing):
    drawing.clear_screen()
    drawing.draw_center_text('Thank you for your time')


def draw(drawing: Drawing, single_shape: bool = False) -> Shape:
    drawing.clear_screen()

    random.shuffle(shapes)
    if single_shape:
        drawing.draw_shape(shapes[0], shapes[0].map(positions[random.randint(0, 3)]))
        target_shape = shapes[0]
    else:
        for index, shape in enumerate(shapes):
            if index > 3:
                break

            position = shape.map(positions[index])
            drawing.draw_shape(shape, position)

        target_shape = shapes[random.randint(0, 3)]
        while target_shape.method == last_shape:
            target_shape = shapes[random.randint(0, 3)]

    heading = f'{current_round}. Please select the {target_shape.type}'
    drawing.draw_heading(heading)

    return target_shape


def draw_third_stage(drawing: Drawing) -> Shape:
    """Draw the next round screen and return the chosen shape"""
    drawing.clear_screen()

    random.shuffle(IAPS)
    figure = IAPS.pop()
    # TODO: improve way to retrieve which image we are using
    image = pygame.image.load(figure)
    SCREEN.blit(image, (0, 0))
    file1 = figure.replace('./IAPS\\', '')
    file2 = file1.replace('.jpeg', '')
    iap = int(file2)
    return iap


def draw_whitespace(drawing: Drawing):
    """Draw the next round screen and return the chosen shape"""
    drawing.clear_screen((255, 255, 255))


shapes = load_shapes()
positions = ["top_left", "top_right", "bottom_left", "bottom_right"]

subject_ID = input('Insert Subject ID')
subject = Subject(subject_ID, date.today(), {})
subject.create_data_template()
time.sleep(5)

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# TODO: Build structure / classes to handle events better
generate_new_round = pygame.USEREVENT + 1
pygame.time.set_timer(generate_new_round, 5000)

max_rounds = 81
current_round = 1
whitespace_rounds = [25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 61,
                     62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 77, 79, 80]
drawing = Drawing()
last_shape = None
winning_shape = draw(drawing)
single_shape = draw(drawing, True)
clickable = True


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == generate_new_round and current_round <= 24:
            current_round = current_round + 1

            if current_round > 81:
                Instance.save_results()
                draw_end_game()
            if current_round < 12:
                Round.set_stage('Game')
                clickable = True
                winning_shape = draw(drawing, False)
                last_shape = winning_shape.type
                continue
            if 12 < current_round < 24:
                Round.set_stage('SingleChoiceGame')
                clickable = True
                single_shape = draw(drawing, True)
                last_shape = single_shape.type
                continue

        if events.type == pygame.MOUSEBUTTONDOWN and current_round <= 12 and clickable is True:
            clicked = SCREEN.get_at(pygame.mouse.get_pos())
            if clicked == winning_shape.colour:
                clickable = False
                print(f"You clicked the {winning_shape.type} successfully.")
                Instance.add_timestamp()
            continue

        if events.type == pygame.MOUSEBUTTONDOWN and 12 < current_round <= 24 and clickable is True:
            clicked = SCREEN.get_at(pygame.mouse.get_pos())
            if clicked == single_shape.colour:
                clickable = False
                print(f"You clicked the {single_shape.type} successfully.")
                Instance.add_timestamp()
            continue

        if 24 < current_round <= 81:
            if current_round not in whitespace_rounds:
                iap = draw_third_stage()
                Round.iap = iap
                Round.switch_stimulation_type()
                Instance.add_timestamp()
                continue
            if current_round in whitespace_rounds:
                Round.switch_stimulation_type()
                Instance.add_timestamp()
                draw_whitespace()
                continue
    pygame.display.update()

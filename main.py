import glob
import json
import os
import random
import sys
from dataclasses import field
from datetime import date

import pygame
from PIL import Image

import factory
import loader
from biosignals import Device, Session, Recording
from recording import SimpleRecording
from shape import Rectangle, Circle, Triangle, Parallelogram, Shape
from subject import Instance
from subject import Round
from subject import Subject

os.environ["SDL_VIDEO_CENTERED"] = "1"

path = './IAPS/*.jpg'

IAPS = []
for filename in glob.glob(path):
    IAPS.append(filename)


def get_iap(file):
    if file == './IAPS\\1.jpg':
        plus = '1'
        return plus
    if file == './IAPS\\2.jpg':
        plus = '2'
        return plus
    if file == './IAPS\\3.jpg':
        plus = '3'
        return plus
    if file == './IAPS\\4.jpg':
        plus = '4'
        return plus
    if file == './IAPS\\5.jpg':
        plus = '5'
        return plus
    if file == './IAPS\\6.jpg':
        plus = '6'
        return plus
    if file == './IAPS\\7.jpg':
        plus = '7'
        return plus
    if file == './IAPS\\8.jpg':
        plus = '8'
        return plus
    if file == './IAPS\\9.jpg':
        plus = '9'
        return plus
    if file == './IAPS\\10.jpg':
        plus = '10'
        return plus
    if file == './IAPS\\11.jpg':
        plus = '11'
        return plus
    if file == './IAPS\\12.jpg':
        plus = '12'
        return plus
    if file == './IAPS\\13.jpg':
        plus = '13'
        return plus
    if file == './IAPS\\14.jpg':
        plus = '14'
        return plus
    if file == './IAPS\\15.jpg':
        plus = '15'
        return plus
    if file == './IAPS\\16.jpg':
        plus = '16'
        return plus
    if file == './IAPS\\17.jpg':
        plus = '17'
        return plus
    if file == './IAPS\\18.jpg':
        plus = '18'
        return plus
    if file == './IAPS\\19.jpg':
        plus = '19'
        return plus
    if file == './IAPS\\20.jpg':
        plus = '20'
        return plus


class Drawing:
    @staticmethod
    def clear_screen(colour: tuple = (0, 0, 0), width: int = 1920, height: int = 1080):
        pygame.draw.rect(SCREEN, colour, (0, 0, width, height))

    @staticmethod
    def draw_center_text(text: str):
        font = pygame.font.Font(None, 48)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(960, 540))
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
        text_rect = text.get_rect(center=(960, 50))
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
    plus = get_iap(figure)
    image = pygame.image.load(figure)
    SCREEN.blit(image, (0, 0))
    return plus


def draw_whitespace(drawing: Drawing):
    """Draw the next round screen and return the chosen shape"""
    drawing.clear_screen((255, 255, 255))


shapes = load_shapes()
positions = ["top_left", "top_right", "bottom_left", "bottom_right"]
subject_ID = input('Insert Subject ID: \n')
today = date.today()
day = today.strftime("%d/%m/%Y")
subject = Subject(subject_ID, day, {})
subject.create_data_template()
Round = Round(['Game', 'SingleChoiceGame', 'Stimulation'], 1, '0', 81, 'Game')
eeg_device = Device(1)
eeg_session = Session(1200, {}, 16, field(default_factory=lambda: [8, 16]), field(default_factory=lambda: ['fs', 'res',
                                                                                                           'source']))
eeg_session.prepare_dict()
eeg = Recording(eeg_session)
SimpleRecording = SimpleRecording()
# BioPlusRecording = BioPlusRecording()
Instance = Instance(subject, SimpleRecording, Round)

start = 0
while start == 0:
    start = input('Ready to start the window? (1 - yes, 0 - no): \n')

pygame.init()
SCREEN = pygame.display.set_mode((1920, 1080))

position_right = 0
while position_right == 0:
    position_right = input('Is the window correctly positioned? (1 - yes, 0 - no): \n')

generate_new_round = pygame.USEREVENT + 1
pygame.time.set_timer(generate_new_round, 5000)

max_rounds = 81
current_round = 1
whitespace_rounds = [25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 61,
                     62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 77, 79, 80]
drawing = Drawing()
last_shape = None
winning_shape = draw(drawing)
clickable = True
stage = 'Game'
Instance.add_timestamp(current_round, stage)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == generate_new_round and current_round <= 81:
            current_round = current_round + 1

            if current_round > 81:
                Instance.save_results()
                draw_end_game(drawing)
            if current_round <= 12:
                Round.set_stage('Game')
                clickable = True
                winning_shape = draw(drawing, False)
                last_shape = winning_shape.type
                stage = 'Game'
                Instance.add_timestamp(current_round, stage)
                continue
            if 12 < current_round <= 24:
                Round.set_stage('SingleChoiceGame')
                clickable = True
                single_shape = draw(drawing, True)
                last_shape = single_shape.type
                stage = 'Game'
                Instance.add_timestamp(current_round, stage)
                continue

        if events.type == pygame.MOUSEBUTTONDOWN and current_round <= 12 and clickable is True:
            clicked = SCREEN.get_at(pygame.mouse.get_pos())
            if clicked == winning_shape.colour:
                clickable = False
                print(f"You clicked the {winning_shape.type} successfully.")
            continue

        if events.type == pygame.MOUSEBUTTONDOWN and 12 < current_round <= 24 and clickable is True:
            clicked = SCREEN.get_at(pygame.mouse.get_pos())
            if clicked == single_shape.colour:
                clickable = False
                print(f"You clicked the {single_shape.type} successfully.")
            continue

        if 25 <= current_round <= 81:
            if current_round not in whitespace_rounds:
                word = draw_third_stage(drawing)
                popular = word
                stage = 'Stimulation'
                Instance.add_timestamp(popular, stage)
                # TODO: figure out why not working dictionary add
                pass

            if current_round in whitespace_rounds:
                draw_whitespace(drawing)
                stage = 'Baseline'
                Instance.add_timestamp(current_round, stage)
                pass

    pygame.display.update()

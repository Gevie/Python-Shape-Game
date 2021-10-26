import pygame
import sys
import os

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

# Width: 800
# Margin: 20
# Gutter: 20
# Column: 370
# Height Grid: 20 - 96 - 20 - 212 - 20 - 212 - 20

PARALLELOGRAM_COLOUR = (0, 0, 0)
TRIANGLE_COLOUR = (255, 255, 0)
RECTANGLE_COLOUR = (0, 176, 240)
CIRCLE_COLOUR = (146, 208, 80)

TOP_LEFT_RECTANGLE_COORDINATES = (105, 192, 200, 100)
TOP_RIGHT_RECTANGLE_COORDINATES = (495, 192, 200, 100)
BOTTOM_LEFT_RECTANGLE_COORDINATES = (105, 424, 200, 100)
BOTTOM_RIGHT_RECTANGLE_COORDINATES = (495, 424, 200, 100)

TOP_LEFT_TRIANGLE_COORDINATES = [(50 + 50, 150 + 150), (150 + 50, 25 + 150), (250 + 50, 150 + 150)]
TOP_RIGHT_TRIANGLE_COORDINATES = [(50 + 450, 150 + 150), (150 + 450, 25 + 150), (250 + 450, 150 + 150)]
BOTTOM_LEFT_TRIANGLE_COORDINATES = [(50 + 50, 150 + 375), (150 + 50, 25 + 375), (250 + 50, 150 + 375)]
BOTTOM_RIGHT_TRIANGLE_COORDINATES = [(50 + 450, 150 + 375), (150 + 450, 25 + 375), (250 + 450, 150 + 375)]

TOP_LEFT_CIRCLE_COORDINATES = (205, 240)
TOP_RIGHT_CIRCLE_COORDINATES = (600, 240)
BOTTOM_LEFT_CIRCLE_COORDINATES = (205, 475)
BOTTOM_RIGHT_CIRCLE_COORDINATES = (600, 475)

TOP_LEFT_PARALLELOGRAM_COORDINATES = [(50 + 75, 150 + 140), (175 + 75, 150 + 140), (225 + 75, 50 + 140), (100 + 75, 50 + 140)]
TOP_RIGHT_PARALLELOGRAM_COORDINATES = [(50 + 450, 150 + 140), (175 + 450, 150 + 140), (225 + 450, 50 + 140), (100 + 450, 50 + 140)]
BOTTOM_LEFT_PARALLELOGRAM_COORDINATES = [(50 + 75, 150 + 375), (175 + 75, 150 + 375), (225 + 75, 50 + 375), (100 + 75, 50 + 375)]
BOTTOM_RIGHT_PARALLELOGRAM_COORDINATES = [(50 + 450, 150 + 375), (175 + 450, 150 + 375), (225 + 450, 50 + 375), (100 + 450, 50 + 375)]


def drawGrid():
    title = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 20, 760, 96))
    top_left_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 136, 370, 212))
    top_right_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (410, 136, 370, 212))
    bottom_left_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (20, 368, 370, 212))
    bottom_right_cell = pygame.draw.rect(SCREEN, (255, 255, 255), (410, 368, 370, 212))

    # top_left_rectangle = pygame.draw.rect(SCREEN, RECTANGLE_COLOUR, TOP_LEFT_RECTANGLE_COORDINATES)
    # top_right_rectangle = pygame.draw.rect(SCREEN, RECTANGLE_COLOUR, TOP_RIGHT_RECTANGLE_COORDINATES)
    # bottom_left_rectangle = pygame.draw.rect(SCREEN, RECTANGLE_COLOUR, BOTTOM_LEFT_RECTANGLE_COORDINATES)
    # bottom_right_rectangle = pygame.draw.rect(SCREEN, RECTANGLE_COLOUR, BOTTOM_RIGHT_RECTANGLE_COORDINATES)

    # top_left_triangle = pygame.draw.polygon(SCREEN, TRIANGLE_COLOUR, TOP_LEFT_TRIANGLE_COORDINATES)
    # top_right_triangle = pygame.draw.polygon(SCREEN, TRIANGLE_COLOUR, TOP_RIGHT_TRIANGLE_COORDINATES)
    # bottom_left_triangle = pygame.draw.polygon(SCREEN, TRIANGLE_COLOUR, BOTTOM_LEFT_TRIANGLE_COORDINATES)
    # bottom_right_triangle = pygame.draw.polygon(SCREEN, TRIANGLE_COLOUR, BOTTOM_RIGHT_TRIANGLE_COORDINATES)

    # top_left_circle = pygame.draw.circle(SCREEN, CIRCLE_COLOUR, TOP_LEFT_CIRCLE_COORDINATES, 75)
    # top_right_circle = pygame.draw.circle(SCREEN, CIRCLE_COLOUR, TOP_RIGHT_CIRCLE_COORDINATES, 75)
    # bottom_left_circle = pygame.draw.circle(SCREEN, CIRCLE_COLOUR, BOTTOM_LEFT_CIRCLE_COORDINATES, 75)
    # bottom_right_circle = pygame.draw.circle(SCREEN, CIRCLE_COLOUR, BOTTOM_RIGHT_CIRCLE_COORDINATES, 75)

    # top_left_parallelogram = pygame.draw.polygon(SCREEN, PARALLELOGRAM_COLOUR, TOP_LEFT_PARALLELOGRAM_COORDINATES)
    # top_right_parallelogram = pygame.draw.polygon(SCREEN, PARALLELOGRAM_COLOUR, TOP_RIGHT_PARALLELOGRAM_COORDINATES)
    # bottom_left_parallelogram = pygame.draw.polygon(SCREEN, PARALLELOGRAM_COLOUR, BOTTOM_LEFT_PARALLELOGRAM_COORDINATES)
    # bottom_right_parallelogram = pygame.draw.polygon(SCREEN, PARALLELOGRAM_COLOUR, BOTTOM_RIGHT_PARALLELOGRAM_COORDINATES)


while True:
    drawGrid()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


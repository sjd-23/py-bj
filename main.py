import pygame as py
from core.model import Model
from core.view import View
from core.controller import Controller

def main():
    # Configuration variables
    window_size = (1280, 720)
    window_caption = "PyBJ"
    window_icon = py.image.load("assets/sprites/cards/s_a.png")
    fps = 144

    # PyGame setup
    py.init()
    py.display.set_caption(window_caption)
    py.display.set_icon(window_icon)
    screen = py.display.set_mode(window_size)
    clock = py.time.Clock()
    font = py.font.Font("assets/fonts/Minecraft.ttf", 32)

    # Model - View - Controller setup
    model = Model()
    view = View(screen, model, font)
    controller = Controller(model, view)

    # Main loop
    while controller.game_running:
        delta_time = clock.tick(fps) / 1000

        controller.update()
        model.update(delta_time)
        view.draw()

if __name__ == '__main__':
    main()
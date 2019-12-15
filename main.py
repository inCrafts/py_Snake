import pygame
from Control import Control
from Snake import Snake
from Gui import Gui
from Food import Food

pygame.init()

window = pygame.display.set_mode((441, 441))
pygame.display.set_caption('Змейка')
control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.init_field()
food.get_food_position(gui)
speed = 0

while control.flag:
    gui.check_finish()
    control.control()
    window.fill(pygame.Color('black'))

    if gui.game == 'GAME':
        snake.draw_snake(window)
        food.draw_food(window)
        gui.draw_indicator(window)
        gui.draw_level(window)

    elif gui.game == 'WIN':
        gui.draw_win(window)

    elif gui.game == 'LOSE':
        gui.draw_lose(window)

    if speed % 100 == 0 and control.pause and gui.game == 'GAME':
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_border()
        snake.animation()
    speed += 1

    pygame.display.flip()


from pico2d import *

open_canvas()


character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def run_circle():
    print('circle')
    pass


def run_rectangle():
    print('rectangle')
    pass






while(True):
    run_rectangle()
    run_circle()



close_canvas()

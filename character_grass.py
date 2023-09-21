from pico2d import *
import math
open_canvas()


character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def run_circle():
    print('circle')
    cx, cy , r = 400, 300, 200
    
    for deg in range(0,360,5):
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)        


    
    pass


def run_rectangle():
    print('rectangle')
    pass






while(True):
    run_rectangle()
    run_circle()
    break



close_canvas()

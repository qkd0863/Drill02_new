from pico2d import *
import math
open_canvas()


character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)


def render_frame(x, y):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)          

def run_circle():
    print('circle')
    cx, cy , r = 400, 300, 200
    
    for deg in range(90,450+1,5):
        x = r * math.cos(math.radians(deg)) + cx
        y = r * math.sin(math.radians(deg)) + cy
        render_frame(x, y)

def run_rectangle():
    print('rectangle')

    
    for x in range(50,750+1,5):
        render_frame(x, 90)
        
    for y in range(90,550+1,5):
        render_frame(750, y)
        
    for x in range(750,50-1,-5):
        render_frame(x,550)
        
    for y in range(550,90-1,-5):
        render_frame(50,y)
    
while(True):
    run_rectangle()
    run_circle()
    break



close_canvas()

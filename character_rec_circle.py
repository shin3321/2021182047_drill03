from pico2d import *
from math import *

def rec_move():
      x= 0
      while (x<770):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 3
            delay(0.01)
      y = 90
      while ( y <550):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(770, y)
            y = y + 3
            delay(0.01)
      x= 770
      while (x>0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 550)
            x = x - 3
            delay(0.01)
      y = 550
      while ( y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, y)
            y = y - 3
            delay(0.01)
      x = 0
      while (x <400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 3
            delay(0.01)
def circle_move():
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(400, 90)
      delay(0.01)
      
      r = 250 
      cx, cy = 370, 300 
      theta = 0  

      while theta < 360:  
            clear_canvas_now()
            grass.draw_now(400, 30)
        
            x = cx + r * math.cos(math.radians(theta))
            y = cy + r * math.sin(math.radians(theta))
        
            character.draw_now(x, y)

            theta += 1
            delay(0.01)

      
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while True:
      rec_move()
      circle_move()

close_canvas()

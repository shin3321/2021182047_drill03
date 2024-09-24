from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
      r,cx,cy = 300, 800//2, 600//2
      for degree in range(0, 360, 3):
            theta = math.radians(degree)
            x = r * math.cos(theta) + cx
            y = r * math.sin(theta) + cy
      
            clear_canvas_now()
            character.draw_now(x, y)
            delay(0.1)

def run_top():
      print("run_top")
      pass

def run_right():
      print("run_right")
      pass

def run_bottom():
      print("run_bottom")
      pass

def run_left():
      print("run_left")
      pass


      
def run_rec():
      print("run_rec")
      run_top()
      run_right()
      run_bottom()
      run_left()

while True:
      run_rec()
      #run_circle()
      break

close_canvas()

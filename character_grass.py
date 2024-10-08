from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x, y):
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x, y)
      delay(0.01)
            
def run_circle():
      r,cx,cy = 300, 800//2, 600//2
      for degree in range(0, 360, 3):
            theta = math.radians(degree)
            x = r * math.cos(theta) + cx
            y = r * math.sin(theta) + cy
      
            draw_boy(x, y)

def run_top():
      print("run_top")
      for x in range (0, 800, 20):
            draw_boy(x, 550)
      pass

def run_right():
      print("run_right")
      for y in range(550, 90, -20):
            draw_boy(790, y)
      pass

def run_bottom():
      print("run_bottom")
      for x in range (800, 0, -20):
            draw_boy(x, 0)
      pass

def run_left():
      print("run_left")
      for y in range(90, 790, 20):
            draw_boy(0, y)
      pass

def run_rec():
      print("run_rec")
      run_top()
      run_right()
      run_bottom()
      run_left()


def tri_bottom():
      print("tri_bottom")
      for x in range(100, 700, 20):
            draw_boy(x, 90)

def tri_right():
      for y in range(90, 400, 20):
            x = 700 - (y-90)
            draw_boy(x, y)
      
def tri_left():
      print("tri_left")
      for y in range (400, 90, -20):
            x = y
            draw_boy(x, y)

def run_tri():
      tri_bottom()
      tri_right()
      tri_left()
      pass

while True:
      run_circle()
      run_rec()
      run_tri()
 

close_canvas()

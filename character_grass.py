from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def run_circle():
      clear_canvas_now()
      character.draw_now(400, 300)
      delay(0.1)
      
def run_rec():
      print("run_rec")


while True:
      run_rec()
      run_circle()
      break

close_canvas()

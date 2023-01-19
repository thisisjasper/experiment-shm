import pygame as pyg
import time
from app import App

def main():
    pyg.init()
    pyg.display.set_caption("physics")
    screen = pyg.display.set_mode((640,640))
    
    running = True
    app_obj = App()
    app_obj.on_start()
    prev_t = time.process_time()
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
                
        curr_t = time.process_time()
        dt = curr_t - prev_t
        app_obj.on_update(dt)
        prev_t = curr_t
        
        app_obj.on_draw(screen)
        pyg.display.flip()
    
if __name__=="__main__":
    main()
import pygame as pyg
from app import app

def main():
    pyg.init()
    pyg.display.set_caption("physics")
    screen = pyg.display.set_mode((640,640))
    running = True
    
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
    
if __name__=="__main__":
    main()
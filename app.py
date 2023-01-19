from physics import World, Body, Vector
from pygame import Surface
import pygame

class App:
    def __init__(self) -> None:
        self.world = World()
        self.body1 = Body()
        self.world.create_body(self.body1)
        self.body1.set_velocity(Vector(100, 0))
        self.body1.set_coords(Vector(300, 300))
        
        pass
    def on_start(self):
        pass
    def on_update(self, dt):
        self.world.time_step(dt)
        pass
    def on_draw(self, screen : Surface):
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 255), self.body1.get_coords().as_tuple(), 25)
        pass
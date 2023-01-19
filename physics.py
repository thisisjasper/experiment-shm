import math

class Vector:
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2
    def magnitude(self):
        return math.sqrt(math.pow(self.v1, 2) + math.pow(self.v2, 2))
    def normalize(self):
        return Vector( (self.v1/self.get_magnitude(), self.v2/self.get_magnitude()) ) 
    def as_tuple(self):
        return (self.v1, self.v2)
    def add(a, b):
        return Vector(a.v1 + b.v1, a.v2 + b.v2)
    def sub(a, b):
        return Vector(a.v1 - b.v1, a.v2 - b.v2)
    def scalar_mult(v, c):
        return Vector(v.v1 * c, v.v2 * c)
        
class Body:
    def __init__(self) -> None:
        self.__mass = 1
        self.__coords = Vector(0,0)
        self.__velocity = Vector(0,0)
        self.__accel = Vector(0,0)
        self.__active = False
        self.resultant_force = Vector(0,0)
    def set_coords(self, vector):
        self.__coords = vector
    def set_velocity(self, vector):
        self.__velocity = vector
    def set_active(self, active):
        self.__active = active
    def set_mass(self, mass):
        self.__mass = mass
    def set_accel(self, accel):
        self.__accel = accel
    def get_coords(self):
        return self.__coords
    def get_velocity(self):
        return self.__velocity
    def get_active(self):
        return self.__active
    def get_mass(self):
        return self.__mass
    def get_accel(self):
        return self.__accel
    def update(self, t):
        self.__velocity = Vector.add(self.__velocity, Vector.scalar_mult(self.__accel, t))
        self.__coords = Vector.add(self.__coords, Vector.scalar_mult(self.__velocity, t))
        
class World:
    def __init__(self) -> None:
        self.__bodies = []
        pass
    def time_step(self, t):
        for body in self.__bodies:
            body.update(t)
        pass
    def create_body(self, body : Body):
        self.__bodies.append(body)
        pass
        
__author__ = 'lmosser'

import parts
import json

class MissingPartException(Exception): pass

class Car(object):
    def __init__(self, type, wheels, engine, body):
        assert(len(wheels) == 4)
        self.type = type
        self.wheels = wheels
        self.engine = engine
        self.body = body

    def start_car(self):
        self.engine.start_engine()
        return True

class Mazda321(Car):
    def __init__(self):
        wheels = [parts.Wheel(16.0) for i in range(1,5)]
        super(Mazda321, self).__init__("Mazda 321", wheels, parts.Engine(), parts.Body(4.5,3.2))

car_imps = [Mazda321]
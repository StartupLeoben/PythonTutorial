__author__ = 'lmosser'

class EngineError(Exception): pass

class Engine(object):
    def __init__(self):
        self.status = "off"

    def start_engine(self):
        if self.status == "on":
            raise EngineError("Engine already on.")

        self.status = "on"
        return self.get_engine_status()

    def get_engine_status(self):
        return self.status

    def shutdown_engine(self):
        if self.status == "off":
            raise EngineError("Engine already off.")

        self.status = "off"
        return self.get_engine_status()

class Wheel(object):
    def __init__(self, diam):
        assert(diam > 0.0)
        self.diameter = diam

class Body(object):
    def __init__(self, length, width):
        assert(length > 0.0)
        assert(width > 0.0)
        self.dimensions = [length, width]
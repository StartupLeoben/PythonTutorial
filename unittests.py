__author__ = 'lmosser'

import unittest
import car
from parts import Engine, EngineError, Wheel, Body
import car_factory

class TestCarFactory(unittest.TestCase):
    def test_json_car_factory(self):
        json_car_factory = car_factory.JSONCarFactory("car_configs.json")
        self.assertEquals(len(json_car_factory.assemble_cars()), 1)

class TestCar(unittest.TestCase):
    def test_start_car(self):
        car1 = car.Car("Random Car", [Wheel(16.5) for i in range(4)], Engine(), Body(16.5, 12.6))
        self.assertTrue(car1.start_car())


class TestBrands(unittest.TestCase):
    #test if all the cars defined in car.py are actually valid cars
    def test_valid_car(self):
        for imp in car.car_imps:
            instance = imp()
            self.assertIsNotNone(instance.type)
            self.assertEqual(len(instance.wheels), 4)
            self.assertNotEqual(instance.engine, None)
            self.assertGreater(instance.body.dimensions[0], 0.0)
            self.assertGreater(instance.body.dimensions[1], 0.0)


class TestEngineBase(unittest.TestCase):
    def test_engine_start_shutdown(self):

        #create the engine
        engine1 = Engine()

        #test if the engine starts
        self.assertEquals(engine1.start_engine(), "on")

        #test if the engine raises an exception if we try to start a started engine
        self.assertRaises(EngineError, engine1.start_engine)

        #test if the engine shuts down
        self.assertEquals(engine1.shutdown_engine(), "off")

        #test if the engine raises an exception if we try to shutdown a stopped engine
        self.assertRaises(EngineError, engine1.shutdown_engine)

if __name__ == '__main__':
    unittest.main()
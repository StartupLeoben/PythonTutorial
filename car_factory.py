__author__ = 'lmosser'
import car
import json
import parts

class JSONCarFactory(object):
    def __init__(self, file_name):
        assert(file_name is not None)

        json_data=open(file_name)
        self.data = json.load(json_data)
        json_data.close()

    def assemble_cars(self):
        cars = []
        for dataset in self.data["cars"]:
            type = dataset["name"]
            wheels = [parts.Wheel(dataset["wheel_diam"]) for i in range(4)]
            engine = parts.Engine()
            body = [parts.Body(length=dataset["body_length"], width=dataset["body_width"])]

            cars.append(car.Car(type, wheels, engine, body))
        return cars




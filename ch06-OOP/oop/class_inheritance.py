class Engine:
    def start(self):
        pass

    def stop(self):
        pass


# ElectricEngine 继承了 start 和 stop 方法
class ElectricEngine(Engine):  # Is A Engine
    pass


# V8Engine 继承了 start 和 stop 方法
class V8Engine(Engine):  # Is A Engine
    pass


class Car:
    engine_cls = Engine  # all instances of car have the same engine

    def __init__(self):
        self.engine = self.engine_cls()  # Has A Engine

    def start(self):
        print(
            "Starting engine {0} for car {1}... Wroom, wroom!".format(
                self.engine.__class__.__name__, self.__class__.__name__
            )
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # RaceCar is A Car
    engine_cls = V8Engine


class CityCar(Car):  # CityCar is A Car
    engine_cls = ElectricEngine


class F1Car(RaceCar):  # F1Car is A RaceCar，F1Car is A Car
    pass


if __name__ == "__main__":
    car = Car()
    race_car = RaceCar()
    city_car = CityCar()
    f1car = F1Car()
    cars = [car, race_car, city_car, f1car]

    for car in cars:
        car.start()

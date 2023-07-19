from engine.engine import Engine
from battery.battery import Battery
from tires.tires import Tires

class Car(Engine, Battery, Tires):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date, current_date, worn_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(worn_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_mileage, last_service_mileage, last_service_date, current_date, worn_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(worn_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(warning_light_is_on, last_service_date, current_date, worn_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(worn_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date, current_date, worn_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(worn_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date, current_date, worn_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(worn_array)
        car = Car(engine, battery, tires)
        return car


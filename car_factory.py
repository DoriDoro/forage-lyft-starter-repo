from datetime import date

from batteries.battery import Battery
from cars.car import Car  # or from cars import car  car.Car
from engines.engine import Engine


class CarFactory(Car, Battery, Engine):
    def create_calliope(
            self,
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int,
    ):
        pass

    def create_glissade(
            self,
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int,
    ):
        pass

    def create_palindrome(
            self, current_date: date, last_service_date: date, warning_light: bool
    ):
        pass

    def create_rorschach(
            self,
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int,
    ):
        pass

    def create_thovex(
            self,
            current_date: date,
            last_service_date: date,
            current_mileage: int,
            last_service_mileage: int,
    ):
        pass

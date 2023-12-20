from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        pass

    def battery_should_be_serviced(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 4)

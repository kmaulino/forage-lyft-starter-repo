import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date.fromisoformat("2018-01-01")
        current_date = date.fromisoformat("2023-01-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2020-01-01")
        current_date = date.fromisoformat("2023-01-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
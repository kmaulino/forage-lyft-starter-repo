import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprime(unittest.TestCase):
    def test_needs_service(self):
        worn_array = [0, 1, 1, 1]
        tires = OctoprimeTires(worn_array)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        worn_array = [0, 0.1, 0.2, 0.3]
        tires = OctoprimeTires(worn_array)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, worn_array):
        self.worn_array = worn_array

    def needs_service(self):
        return sum(self.worn_array) >= 3
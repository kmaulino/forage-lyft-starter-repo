from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, worn_array):
        self.worn_array = worn_array

    def needs_service(self):
        return any(w >= 0.9 for w in self.worn_array)
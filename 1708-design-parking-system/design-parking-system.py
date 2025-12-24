class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # We store the capacities in a list. 
        # We add a '0' at the start so index 1 corresponds to carType 1, 
        # index 2 to carType 2, etc.
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        # Check if there is space available for this specific carType
        if self.slots[carType] > 0:
            self.slots[carType] -= 1  # Park the car (reduce available space)
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
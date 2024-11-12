class Lift:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.position = lowest

    def move_to(self, destination):
        if destination > self.position:
            self.move_up(destination)
        elif destination < self.position:
            self.move_down(destination)

    def move_up(self, target):
        while self.position < target and self.position < self.highest:
            self.position += 1
            print(f"Now at floor {self.position}")

    def move_down(self, target):
        while self.position > target and self.position > self.lowest:
            self.position -= 1
            print(f"Now at floor {self.position}")

# Test
lift = Lift(0, 10)
lift.move_to(5)
lift.move_to(0)
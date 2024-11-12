class Lift:
    def __init__(self, lowest, highest):
        self.position = lowest
        self.lowest, self.highest = lowest, highest

    def move_to(self, floor):
        while self.position < floor: self.up()
        while self.position > floor: self.down()

    def up(self):
        if self.position < self.highest:
            self.position += 1
            print(f"At floor {self.position}")

    def down(self):
        if self.position > self.lowest:
            self.position -= 1
            print(f"At floor {self.position}")

class Tower:
    def __init__(self, lowest, highest, lift_count):
        self.lifts = [Lift(lowest, highest) for _ in range(lift_count)]

    def operate_lift(self, lift_num, floor):
        print(f"\nMoving Lift {lift_num} to floor {floor}")
        self.lifts[lift_num].move_to(floor)

    def emergency(self):
        print("\nEmergency! Sending all lifts to the ground floor.")
        for idx, lift in enumerate(self.lifts):
            print(f"\nLift {idx} moving to floor {lift.lowest}")
            lift.move_to(lift.lowest)

# Test
if __name__ == "__main__":
    tower = Tower(0, 10, 3)
    tower.operate_lift(0, 5)
    tower.operate_lift(1, 8)
    tower.emergency()


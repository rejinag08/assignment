class Lift:
    def __init__(self, min_floor, max_floor):
        self.position = min_floor
        self.min_floor, self.max_floor = min_floor, max_floor

    def move_to(self, destination):
        while self.position < destination:
            self.ascend()
        while self.position > destination:
            self.descend()

    def ascend(self):
        if self.position < self.max_floor:
            self.position += 1
            print(f"Currently on floor {self.position}")

    def descend(self):
        if self.position > self.min_floor:
            self.position -= 1
            print(f"Currently on floor {self.position}")

class Tower:
    def __init__(self, min_floor, max_floor, elevator_count):
        self.lifts = [Lift(min_floor, max_floor) for _ in range(elevator_count)]

    def operate_lift(self, lift_index, target_floor):
        print(f"\nOperating lift {lift_index} to reach floor {target_floor}")
        self.lifts[lift_index].move_to(target_floor)

# Test
tower = Tower(0, 10, 3)
tower.operate_lift(0, 5)
tower.operate_lift(1, 8)
tower.operate_lift(0, 0)
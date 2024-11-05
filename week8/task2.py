class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

# Main Program
car = Car("ABC-123", 142)

# Step 1: Accelerate the car in the specified steps
car.accelerate(30)   # Increase speed by +30 km/h
car.accelerate(70)   # Increase speed by +70 km/h
car.accelerate(50)   # Increase speed by +50 km/h

# Step 2: Print out the current speed
print("Current Speed after accelerations:", car.current_speed, "km/h")

car.accelerate(-200)

# Step 4: Print out the final speed
print("Final Speed after emergency brake:", car.current_speed, "km/h")
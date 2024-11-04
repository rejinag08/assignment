class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0  # Automatically set to 0 for every new car
        self.travelled_distance = 0  # Automatically set to 0 for every new car

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Main Program
car = Car("ABC-123", 142)

# Set some speed and drive
car.accelerate(60)  # Accelerate to 60 km/h
car.drive(1.5)      # Drive for 1.5 hours
print("Travelled Distance:", car.travelled_distance, "km")
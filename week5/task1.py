
import random
num_dice = int(input("How many dice to roll? "))
# Initialize sum variable
total_sum = 0
# Roll dice and calculate the sum
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll
#printing the result
print(f"Sum of rolls: {total_sum}")
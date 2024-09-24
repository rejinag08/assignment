#Create a program using a while loop that prints all numbers divisible by three within the range of 1 to 1000.
number=3
while number<=1000:
    if number % 3 == 0:
        print(number)
    number += 1

# Initialize an empty list to store the numbers
numbers = []
#asking the user for numbers until they input an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(int(user_input))

numbers.sort(reverse=True)

top_five = numbers[:5]

# Print the result
print("The five greatest numbers are:", top_five)
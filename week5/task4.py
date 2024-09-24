#empty list to store the city names
cities = []
# Use a for loop to ask user for five city names
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)
# Use a for/in loop to print the city names one by one
print("\nThe cities you entered are:")
for city in cities:
    print(city)
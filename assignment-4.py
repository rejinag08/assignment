#ask users for the three integer numbers
num1 = int(input("Enter the first numer: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third numbers: "))
#calculate the sum
sum_of_numbers = num1 + num2 +num3
#calculate the product
product_of_numbers = num1 * num2 * num3
#calculate the average
average_of_numbers = sum_of_numbers /3
#print
print(f"the sum of the numbers is {sum_of_numbers}")
print(f"the product of the numbers is {product_of_numbers}")
print(f"the average of the numbers is {average_of_numbers:.2f}")

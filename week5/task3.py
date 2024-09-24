#check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter an integer: "))
# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
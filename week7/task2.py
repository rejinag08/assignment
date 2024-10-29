def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 gallon ≈ 3.78541 liters

def main():
    while True:
        try:
            gallons = float(input("Enter gasoline volume in gallons (negative to exit): "))
            if gallons < 0:
                print("Exiting the program.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is approximately {liters:.2f} liters.")
        except ValueError:
            print("Please enter a valid number.")
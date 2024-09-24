def pizza_unit_price(diameter_cm, price_euros):
    radius_m = diameter_cm / 2 / 100
    area_m2 =math.pi * (radius_m ** 2)
    return price_euros / area_m2

def main():
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (euros): "))

    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (euros): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"\nUnit price of first pizza: {unit_price1:.2f} €/m²")
    print(f"Unit price of second pizza: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")
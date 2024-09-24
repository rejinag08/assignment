# Cruise Ship Cabin Class Description Program
# Ask user to input the cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()
# Check the cabin class and print
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Cabin above the car deck with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

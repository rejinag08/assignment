# Hemoglobin Level Checker Program

# Ask for user's biological gender
gender = input("Enter your biological gender (male/female): ").lower()

# Ask for user's hemoglobin level
try:
    hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))

    # Check the gender and hemoglobin level
    if gender == "female":
        if hemoglobin_level < 117:
            print("Your hemoglobin level is low.")
        elif 117 <= hemoglobin_level <= 155:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")
    elif gender == "male":
        if hemoglobin_level < 134:
            print("Your hemoglobin level is low.")
        elif 134 <= hemoglobin_level <= 167:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")
    else:
        print("Invalid gender input.")
except ValueError:
    print("Invalid hemoglobin level. Please enter a numeric value.")

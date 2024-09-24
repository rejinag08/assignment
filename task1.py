# Ask the fisher for the length of the zander
try:
    zander_length = float(input("Enter the length of the zander in centimeters: "))

    # Legal size limit for zander is 42 cm
    legal_size_limit = 42

    # Check if the zander is below or above the legal limit
    if zander_length < legal_size_limit:
        short_by = legal_size_limit - zander_length
        print(f"The zander is too small. Please release it back into the lake.")
        print(f"It is {short_by:.1f} centimeters short of the legal limit.")
    else:
        print("The zander meets the legal size limit. You may keep it.")
except ValueError:
    print("Invalid input. Please enter a numeric value for the length.")

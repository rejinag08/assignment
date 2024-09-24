# Conversion factors
LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20
GRAMS_IN_KILOGRAM = 1000

#Ask the user for talents, pounds, and lots
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

#Convert everything to grams
# Convert talents to pounds, pounds to lots, and then lots to grams
total_lots = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS) + (pounds * POUND_TO_LOTS) + lots
total_grams = total_lots * LOT_TO_GRAMS

#Convert grams to kilograms and remaining grams
kilograms = int(total_grams // GRAMS_IN_KILOGRAM)  # Whole kilograms
grams = total_grams % GRAMS_IN_KILOGRAM  # Remaining grams

#print the result
print(f"The weight in modern units: {kilograms} kilogram
min_number = 0
max_number = 0
while True :
    number = int(input("Enter a number"))
    if number == "":
        break
     elif int(number) < min_number or min_number == 0:
        min_number = int(number)
    elif int(number) > max_number or max_number == 0:
      max_number = int(number)


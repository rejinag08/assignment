x= float (input("enter the value to change from inches to centimeters:"))
while x>=0:
    cm = x*2.54
    print(f"{x} inches is {cm} centimeters")
    x = float(input("enter the value to change from inches to centimeters:"))
if x<0:
    print ("sorry negative value entered")

print("Step 1: Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Car")
choice=int(input("Enter 1 or 2:"))
print()
if choice == 1:
    print("Pick your bike")
    print(" 1 - Mountain bike")
    print(" 2 - Scooty")
    two_wheeler=int(input("Enter 1 or 2:"))
    print()

    if two_wheeler == 1 :
        print("YOUR pick is SCOOTY")
        print("Top speed only 60 km/h")
        print("Best for  :City roads")
    else:
        print("You picked the bike")
        print("Yop speed :30 kh/h")
        print("Best for :off road drives")

elif choice == 2:
    print("Pick your car")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    four_wheeler=int(input("Enter 1 or 2:"))
    print()

    if four_wheeler == 1 :
        print("YOUR pick is Sedan")
        print("No. of seats :5")
        print("Best for  :City roads")
    else:
        print("You picked the SUV")
        print("No. of seats :7")
        print("Best for :off road drives")
else:
    print("Invalid data \n Please enter 1 for bike or 2 for car")
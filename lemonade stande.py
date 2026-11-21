def greet_customer():
    print("Welcome to the lemonade stand")
    print("Fesh lemons, made just for YOU!")
greet_customer()
pricePerCup = float(input('Enter the price per cup'))
NoOfCups = int(input("Enter the no. of cups sold"))
def calculate_total(price,cups):
    total = price * cups
    return total
total_cost = calculate_total(pricePerCup,NoOfCups)
rounded_total = round(total_cost,2)
print("Total Cost:",rounded_total)
amountPaid=float(input('Enter the amount paid by rhe customber:'))
def calculate_change(paid,total):
    change= paid - total
    return change
change_due = calculate_change(amountPaid,rounded_total)
rounded_change = round(change_due,2)
def thank_you_message(cups):
    if cups >= 5:
        return "Wow, big order! Thank you so much"
    else:
        return"Thanks for stopping by the stand!"
closing_message = thank_you_message(NoOfCups)
print("")
print("=====Lemonade Stand Receipt=====")
print("Price Per Cup",pricePerCup)
print("Cups Sold",NoOfCups)
print("Total Cost",rounded_total)
print("Amount Paid",amountPaid)
print("Change Due",rounded_change)
print(closing_message)
print("================================")
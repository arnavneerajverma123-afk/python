def greet_customer():
    print("Welcome to the lemonade stand")
    print("Fresh lemonade , made just for you")
greet_customer()
price=float(input("Enter price in rupees:"))
soldcups = int(input("Enter the no. of cups"))
def calculate_total(price,cups):
    total = price*cups
    return total
total_cost=calculate_total(price,soldcups)
rounded_total=round(total_cost,2)
print("total cost:",rounded_total)
amount_paid=float(input("Enter amount paid:"))
def calculate_change(paid,total):
    change=paid-total
    return change
change_due= calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)
def thanks_message(cups):
    if cups>=5:
        return "Wow,big order"
    else:
        return "Thanks"
message = thanks_message(soldcups)
    
print("")
print("===LEMONADE STAND RECEIPT===")
print("PRICE",price)
print("cups",soldcups)
print("total",rounded_total)
print("amount paid",amount_paid)
print("Change",rounded_change)
print(message)
print("=========================================")

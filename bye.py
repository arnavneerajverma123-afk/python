valid = False
while not valid:
    try:
        n=int(input("Enter a no. :"))
        while n%2==0:
            print("bye")
            n=n+1
        valid = True
    except ValueError:
        print("Invalid")

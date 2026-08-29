try:
    no = int(input("Enter a no.:"))
    print("the no. is:",no)
except ValueError as ex:
    print("exception",ex)
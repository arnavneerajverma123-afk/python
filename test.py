a=int(input("Enter no."))
b=int(input("enter another no."))
try:
    print(a+b,a-b,a*b,a/b)
except ZeroDivisionError or ValueError :
    print('either you kept it as a 0 or you kept a non number')





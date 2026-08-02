print("Half Pyramid Pattern of numbers (1234 ):")
n=int(input("Enter a no.:"))
for i in range(n):
    for j in range(i+1):
        print(i ,end="")
    print()
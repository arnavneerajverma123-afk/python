print("Half Pyramid Pattern of stars (*):")
n=int(input("Enter a no.:"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()
print("===WELCOME TO GUESS THE NUMBER===")
secret=27
num=int(input("Enter a number"))
attempts=5
if num != secret and num > secret :
    print("wrong by",num-secret)
    attempts-1
    if attempts==0:
        print(end="Game over")
elif num != secret and num < secret :
    print("wrong by",secret-num)
    attempts-1
    if attempts ==0:
        print(end="Game over")
elif num == secret :
    print("correct it was:",secret,"you used",5-attempts,"attempts only")
    
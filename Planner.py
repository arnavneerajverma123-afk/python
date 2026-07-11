print("=== Smart School Day Planner === ")
print("Answer 3 quick questions and i'll plan your day!\n ")
day=input("What day of the week is it? (e.g. Monday, Friday, Weekend ,Other School days etc.): ").strip().capitalize()
weather=input("Whats the weather like today? (e.g. Sunny, Rainy, Cloudy): ").strip().lower()
Homework=input("Do you have any homework due today? (Yes/No): ").strip().lower()
if day in ("Saturday", "Sunday"):
    print("Day type : Weekend - enjoy your free time!")

elif day == "Monday":
    print("Day type : First day of the week.")

elif day == "Friday":
    print("Day type : Last school day.")

elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type : Regular school day.")
else:
    print("Day type : Day not recognised.")
if weather == "sunny" and Homework =="yes":
    print("After school: Go to the park and enjoy the sunshine,")
if weather == "rainy" or weather == "cloudy" :
    print("Carry an umberlla - it may or may not rain")
if not (Homework=="yes"):
    print("After school: Do your homework or get scoldings.")
if weather == "rainy" and not (Homework == "yes"):
    print("Best plan : Stay in, finish homework first.")

elif weather == "sunny" and Homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day!")

elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend - head outside!")
else:
    print("Best plan : Take it one step at a time!")
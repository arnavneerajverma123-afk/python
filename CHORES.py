total_chores=4
orignal_count=total_chores
count=0
chores=1
while chores<=total_chores:
    if chores == 1 : next_chore = "Make your bed"
    elif chores == 2 : next_chore = "Feed pet"
    elif chores == 3 : next_chore = "Take out the trash"
    else: next_chore = "Wash Dishes"
    answer = input(f"Have you finished : {next_chore}? (yes/no):")
    if answer=="yes":
        count += 1 
        chores += 1
        print("nice")
    else:
        print('finish the chores')
    print('chores remaning:',total_chores-count)
print("you are free")


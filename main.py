import random
'''
In this Game, 
1 = Snake,
0 = Water,
-1 = Gun
'''

computer = random.choice([-1, 0, 1])
user_choice = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youDict = {"s": 1, "w": 0, "g": -1}
reverseDict = {1: "Snake", 0: "Water", -1: "Gun"}

if user_choice not in youDict:
    print("Invalid input!")
else:
    you = youDict[user_choice]
    print(f"Computer chose: {reverseDict[computer]}")
    print(f"You chose: {reverseDict[you]}")

    if computer == you:
        print("It's a tie!")
    elif (computer == 1 and you == 0) or (computer == 0 and you == -1) or (computer == -1 and you == 1):
        print("You Lose.")
    elif (computer == 0 and you == 1) or (computer == -1 and you == 0) or (computer == 1 and you == -1):
        print("You Win.")
    else:
        print("Something Went Wrong...")
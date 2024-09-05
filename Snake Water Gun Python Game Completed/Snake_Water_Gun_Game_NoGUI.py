import random # This is the Package for Randomdity in game
              # It is Just like Header files of C language with some different Perspective

p_score = 0 #This is the scre counter

# Below are the Conditions when user wins or loses
# The Number representation is as follows:
# 1 --> Snake
# 2 --> Water
# 3 --> Gun
def check(user, comp):
    if(user == comp):
        return 0
    elif(user == 1 and comp == 2):
        return 1
    elif(user == 2 and comp == 3):
        return 1
    elif(user == 3 and comp == 1):
        return 1
    else:
        return -1


# This is taking input from user
usert   = input("Snake, Water, Gun:\n")
user = 0

# This will choose random numbers between 1 and 3
comp   = random.randint(1, 3)

# I don't Know how to explain you.
# I was trying to convert string input by user in variable usert into number (1-3) and store in another variable as user
if(usert == "snake" or usert == "Snake"):
    user = 1
elif(usert == "water" or usert == "Water"):
    user = 2
elif(usert == "gun" or usert == "Gun"):
    user = 3

# Here I was Repeating the above process but this time for computer in reverse.
# the number by computer in random and is converted into the corresponding String (Snake, Gun, Water) to show output from Computer on Screen

if(comp == 1):
    compt = "Snake"
elif(comp == 2):
    compt = "Water"
elif(comp == 3):
    compt = "Gun"

# From Here Comes The Main Logic

# This shows values of user and computer on screen
print(f"\nYou: \t\t{usert}\nComputer: \t{compt}")

# The following code shows and calculates score on screen
# It also determines Whether You have won, lost or it's a draw.
score = check(user, comp)
p_score = p_score+score
if(score == 0):
    print(f"It's a Draw!\nScore: {p_score}\n")
elif(score == 1):
    print(f"You Win!\nScore: {p_score}\n")
elif(score == -1):
    print(f"You Lose!\nScore: {p_score}\n")

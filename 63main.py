import random

def check(comp, user):
    if comp == user:
        return 0
    elif comp == 0 and user == 1:
        return -1
    elif comp == 1 and user == 2:
        return -1
    elif comp == 2 and user == 0:
        return -1
    else:
        return 1

comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water, 2 for Gun:\n "))

print("Computer chose:", comp)

score = check(comp, user)

print("you: ", user)
print("computer: ", comp)

if score == 0:
    print("It's a draw")
elif score == -1:
    print("You lose")
else:
    print("You win")
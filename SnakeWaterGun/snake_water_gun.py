import random
lst = ("Snake","Water","Gun")
comp = random.choice(lst)
print("---Welcome To The Game (Snake Water Gun)---")
n = int(input("Please enter number of chances you want to play: "))
comp_point = 0
user_point = 0
i = 0
while i<n:
    input_1 = input("Please enter s for Snake, w for Water, g for Gun: ")
    if input_1 == "s":
        choice = "Snake"
        if comp == choice:
            print("It's a Tie,\nPlease try again")
        elif comp == "water":
            user_point = user_point + 1
            print("Hurrah! you won")
        elif comp == "Gun":
            comp_point = comp_point + 1
            print("oh! you loose,\nplease try again")
    elif input_1 == "w":
        choice = "Water"
        if comp == choice:
            print("It's a Tie,\nPlease try again")
        elif comp == "Gun":
            user_point = user_point + 1
            print("Hurrah! you won")
        elif comp == "Snake":
            comp_point = comp_point + 1
            print("oh! you loose,\nplease try again")
    elif input_1 == "g":
        choice = "Gun"
        if comp == choice:
            print("It's a Tie,\nPlease try again")
        elif comp == "Snake":
            user_point = user_point + 1
            print("Hurrah! you won")
        elif comp == "Water":
            comp_point = comp_point + 1
            print("oh! you loose,\nplease try again")
    else:
        print("Invalid Input entered")
    i = i + 1

print("----SCORECARD----")
if comp_point>user_point:
    print("-->Computer won the game<--")
elif comp_point == user_point:
    print("-->Wow! it's a tie<--")
else:
    print("-->Congo! You won the game<--")


"""
Instructions:
Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, A message should display "What you want to log. Diet or Exercise"
Use function
"""


# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
"""
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)
"""

"""
def log(n):
    if n==1:
        c = int(input("Enter 1 for exercise or 2 for Food"))
        if c==1:
            d = input("Please enter the name of exercise")
            with open("Hotel_mang_ex_1","a") as o:
                o.write(str([str(getdate())])+" : "+d)
            print("Data added Successfully")
        elif c==2:
            d = input("Please enter the name of food")
            with open("Hotel_mang_food_1", "a") as o:
                o.write(str([str(getdate())]) + " : " + d)
            print("Data added Successfully")
    elif n==2:
        c = int(input("Enter 1 for exercise or 2 for Food"))
        if c == 1:
            d = input("Please enter the name of exercise")
            with open("Hotel_mang_ex_2", "a") as o:
                o.write(str([str(getdate())]) + " : " + d)
            print("Data added Successfully")
        elif c==2:
            d = input("Please enter the name of food")
            with open("Hotel_mang_food_2", "a") as o:
                o.write(str([str(getdate())]) + " : " + d)
            print("Data added Successfully")
    elif n==3:
        c = int(input("Enter 1 for exercise or 2 for Food"))
        if c == 1:
            d = input("Please enter the name of exercise")
            with open("Hotel_mang_ex_3", "a") as o:
                o.write(str([str(getdate())]) + " : " + d)
            print("Data added Successfully")
        elif c==2:
            d = input("Please enter the name of food")
            with open("Hotel_mang_food_3", "a") as o:
                o.write(str([str(getdate())]) + " : " + d)
            print("Data added Successfully")


def retrieve(l):
    if l==1:
        z = int(input("Enter 1 for exercise or 2 for Food"))
        if z==1:
            with open("Hotel_mang_ex_1","r") as o:
                print(o.read())
        elif z==2:
            with open("Hotel_mang_food_1","r") as o:
                print(o.read())
    elif l==2:
        z = int(input("Enter 1 for exercise or 2 for Food"))
        if z==1:
            with open("Hotel_mang_ex_2","r") as o:
                print(o.read())
        elif z==2:
            with open("Hotel_mang_food_2","r") as o:
                print(o.read())
    elif l==3:
        z = int(input("Enter 1 for exercise or 2 for Food"))
        if z==1:
            with open("Hotel_mang_ex_3","r") as o:
                print(o.read())
        elif z==2:
            with open("Hotel_mang_food_3","r") as o:
                print(o.read())

print("Health Management System")
a = int(input("Press 1 for log the value and 2 for retrieve"))
if a==1:
    b = int(input("Enter 1 for A, 2 for B, 3 for C"))
    log(b)
else:
    b = int(input("Enter 1 for A, 2 for B, 3 for C"))
    retrieve(b)
"""

"""
def log(n):
    a = int(input("Press 1 for log the value and 2 for retrieve"))
    if a == 1:
        c = int(input("Enter 1 for exercise or 2 for Food"))
        if c==1:
            d = input("Please enter the name of exercise")
            with open("Hotel_mang_"+str(c)+"_"+str(n),"a") as o:
                o.write(str([str(getdate())])+" : "+d)
                print("Data added Successfully")
        elif c==2:
            d = input("Please enter the name of food")
            with open("Hotel_mang_"+str(c)+"_"+str(n),"a") as o:
                o.write(str([str(getdate())]) + " : " + d)
                print("Data added Successfully")
    elif a==2:
        if c == 1:
            d = input("Please enter the name of exercise")
            with open("Hotel_mang_" + str(c) + "_" + str(n), "r") as o:
                print(o.read())
        elif c == 2:
            d = input("Please enter the name of food")
            with open("Hotel_mang_" + str(c) + "_" + str(n), "r") as o:
                print(o.read())


print("Health Management System")
b = int(input("Press 1 for A, 2 for B, 3 for C "))
log(b)
"""


"""def log(n):
    c = int(input("Enter 1 for exercise or 2 for Food"))
    if c == 1:
        choice = "exercise"
    elif c == 2:
        choice = "food"

    d = input("Please enter the name of " + choice + ":")
    with open("Hotel_mang_" + choice + "_" + str(n) , "a") as o:
        o.write(str([str(getdate())]) + " : " + d)
    print("Data added Successfully")


def retrieve(n):
    z = int(input("Enter 1 for exercise or 2 for Food"))
    if z == 1:
        choice = "exercise"
    elif z == 2:
        choice = "food"
    with open("Hotel_mang_" + choice + "_" + str(n) , "r") as o:
        print(o.read())

print("Health Management System")
a = int(input("Press 1 for log the value and 2 for retrieve"))
if a == 1:
    b = int(input("Enter 1 for A, 2 for B, 3 for C"))
    log(b)
else:
    b = int(input("Enter 1 for A, 2 for B, 3 for C"))
    retrieve(b)"""

def operation(optionType,userId):
    choiceId = int(input("Enter 1 for exercise or 2 for Food"))
    if choiceId == 1:
        choice = "exercise"
    elif choiceId == 2:
        choice = "food"
    if optionType == 1:
        choiceType = input("Please enter the name of " + choice + ":")
        with open("Health_mang_" + choice + "_" + str(userId), "a") as o:
            o.write(str([str(getdate())]) + " : " + choiceType + "\n")
        print("Data added Successfully")
    elif optionType==2:
        with open("Health_mang_" + choice + "_" + str(userId), "r") as o:
            print(o.read())

print("Health Management System")
optionType = int(input("Press 1 for log the value and 2 for retrieve: "))
userId = int(input("Enter 1 for A, 2 for B, 3 for C: "))
operation(optionType,userId)

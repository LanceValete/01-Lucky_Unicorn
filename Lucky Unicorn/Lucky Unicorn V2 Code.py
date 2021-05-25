import random

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n": 
            response = "no"
            return response

        else:
            print("Please answer yes / no")

def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

def num_check(question, low, high):

    error = "Please enter an whole number between 1 and 10"

    vaild = False
    while not vaild:
        try:
            response = int(input(question))

            if low < response <= high:
                return response
                
            else:
                print(error)

        except ValueError:
            print(error)

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

print()
play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    rounds_played += 1

    print()
    print("*** Round #{} ***".format(rounds_played))
    
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "horse"

        else:
            chosen = "zebra"
        balance -= 0.5

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:    
        print("You got a {}. Your balance: ${:.2f}".format(chosen, balance))
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
print("Final balance ${}".format(balance))
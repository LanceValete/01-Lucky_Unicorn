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
    print("How to Play", "*")
    print()
    print("Choose a starting speanding amount (minimum $1, maxiumum $10).")
    print()
    print("Then press <enter> to begin playing. You will either get a horse, \n"
            "zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win \n"
    "some of the money back. Here's the payout amounts:\n\n"
    "Unicorn: $5.00 (balance increases by $4)\n"
    "Horse: $0.50 (balance decreases by $0.50)\n"
    "Unicorn: $0.50 (balance decreases by $0.50)\n"
    "Unicorn: $0.00 (balance decreases by $1)\n")

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

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

statement_generator("Welcome to the Lucky Unicorn Game", "*")

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
    statement_generator("Round #{}".format(rounds_played), ".")
    print()
    
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        else:
            chosen = "zebra"
            prize_decoration = "Z"
            balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        statement_generator("Sorry you have run out of money", "L")

    else:    
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
statement_generator("Result", "=")
print("Final balance ${}".format(balance))

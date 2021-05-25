import random

# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n": 
            response = "no"
            return response

        # If response is anything else, output 'error'
        else:
            print("Please answer yes / no")

def instructions():
    print()
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting spending amount (minimum $1, maxiumum $10).")
    print()
    print("Then press <enter> to begin playing. You will either get a horse, \n"
            "zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win \n"
    "some of the money back. Here's the payout amounts:\n\n"
    "Unicorn: $5.00 (balance increases by $4)\n"
    "Horse: $0.50 (balance decreases by $0.50)\n"
    "Zebra: $0.50 (balance decreases by $0.50)\n"
    "Donkey: $0.00 (balance decreases by $1)\n")

    return ""

def num_check(question, low, high):

    error = "Please enter an whole number between 1 and 10"

    vaild = False
    while not vaild:
        try:
            #ask the question 
            response = int(input(question))

            # valid response
            if low < response <= high:
                return response
            
            # if the amount is too low / too high output an error
            else:
                print(error)

        #if there is an error, in this case strings or floats, this code will play
        except ValueError:
            print(error)

def statement_generator(statement, decoration):
    # stars that go at sides of statement
    sides = decoration * 3

    # putting the statement and stars in one line
    statement = "{} {} {}".format(sides, statement, sides)

    # stars that go at the top and bottom of statement
    top_bottom = decoration * len(statement)

    # putting the top/bottom 
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with... 
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

# set balance for testing purposes
balance = how_much

rounds_played = 0

print()
play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    # increase no. of rounds played
    rounds_played += 1

    # print round number
    print()
    statement_generator("Round #{}".format(rounds_played), ".")
    print()
    
    chosen_num = random.randint(1, 100)

    # Adjust balance 
  # if the random no. is between 1 and 5, user gets a unicorn (add $4 to the balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random no. is between 6 and 36, user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # the token is either a horse or a zebra, in either case subtract $0.50 from balance
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
            balance -= 0.5

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
            balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print()
        print("You have run out of money!")
        print()
        statement_generator("Game Over", "#")
        print()

    else:    
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
statement_generator("Result", "=")
print("Final balance ${:.2f}".format(balance))
print()


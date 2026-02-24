# functions here
def yes_no(question):
    while True:
        response = input(question).lower()

        # check response,
        # check if user says yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter 'yes' or 'no'")


def instruction():
    print('''
    
**** Instructions ****

To begin, choose the nuber of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

 Good Luck.

    ''')


# Main routine
print()
print("📈📈📈 Welcome to the Higher or Lower Game 📉📉📉")
print()

# loop for testing purposes

want_instructions = yes_no("Would you like to read the instructions?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
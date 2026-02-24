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



# checks for int more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer more than 1."

        to_check = input(question)

        # check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check if response more than 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# Initialize game variables
mode = "regular"
rounds_played = 0


print("📈📈📈 Welcome to the Higher or Lower Game 📉📉📉")
print()

want_instructions = yes_no("Would you like to read the instructions?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds? Or, push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # HEADINGS
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # if user choice is exit code, break
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# game loop ends here

# game history / stats area

# auto testing
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

# run test
for i in to_test:
    # retrieve test case
    case = i[0]
    expected = i[1]

    #  get actual value
    actual = int_check(case)

    # comparing
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")

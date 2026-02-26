import math
import random


# yes no
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
secret number will be between 1 and 10).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

 Good Luck.

    ''')


# checks for int with optional upper
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    # if any int is allowed
    if low is None and high is None:
        error = "Please enter a valid integer."

    # if the number needs to be more than an
    # integer
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"greater than or equal to {low}.")

    # if number needs to be between low & high
    else:
        error = (f"Please enter an integer that is "
                 f"between {low} and {high} (inclusive).")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # check int not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return
            else:
                return response

        except ValueError:
            print(error)


# calc the max number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# main routine here

# Initialize game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("📈📈📈 Welcome to the Higher or Lower Game 📉📉📉")
print()

want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":        # REMEMBER TO REO-MOVE THE INFINITE
    mode = "infinite"
    num_rounds = 5

# get game parameters
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose high / low number
else:
    low_num = int_check("Low number? ")
    high_num = int_check("High number? ", low=low_num + 1)

# calc max number of guesses
guesses_allowed = calc_guesses(low_num, high_num)

# game loop starts here
while rounds_played < num_rounds:

    # HEADINGS
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)

    # round starts here
    # set guessed used to 0 at start of every round
    guesses_used = 0
    already_guessed = []

    # choose a secret number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)      # remove this line after testing!

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask user to guess
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You have already guessed {guess}.   You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a dupe
        else:
            already_guessed.append(guess)

        # add one
        guesses_used += 1

        # compare users guess with the secret number

        # if we have guesses left
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses.")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses.")

        # when secret number is guessed, we have three different feedback
        # options
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses. "
            else:
                feedback = f"Well done! you guessed the secret number in {guesses_used} guesses."

        # if no guesses
        else:
            feedback = "Sorry, you didn't guess the secret number. You lose this round!"


        # print feedback
        print(feedback)

        # additional feedback
        if guesses_used == guesses_allowed - 1:
            print("\n❗❗❗ Careful - you have one guess left! ❗❗❗\n")

    print()

    # Round ends here

    # if user has entered exit code, END GAMEE!!!
    if end_game == "yes":
        break


    # add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"

    game_history.append(history_feedback)

    rounds_played += 1
    all_scores.append(guesses_used)                # josh check if you have this

# check users have played at least one round
# before calculating stats.
if rounds_played > 0:
    # history / stats area

    # calculate stats
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # output the stats
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"Best: {best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see the game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)
            print()
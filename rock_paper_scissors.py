import random


def main():
    user_points = 0
    computer_points = 0
    valid_values = [
        "rock",
        "paper",
        "scissors",
    ]
    print("Let's play Rock/Paper/Scissors")
    agreement = get_agreement()
    if agreement == False:
        quit()

    try:
        print("Press Ctrl+D or Enter q to exit")
        while True:
            user_input = input("Please type Rock, Paper or Scissors: ").strip().lower()
            if user_input == "q":
                raise EOFError
            elif user_input not in valid_values:
                print("Please input a valid value.")
                continue
            else:
                computer_random_pick = random.choice(valid_values)
                print(f"Computer picked {computer_random_pick}.")
                user_points, computer_points = rock_paper_scissors(
                    user_input, computer_random_pick, user_points, computer_points
                )

    except EOFError:
        print(f"You scored {user_points} points!")
        print(f"The computer scored {computer_points} points!")

        if user_points > computer_points:
            print("You have won!")
        elif user_points == computer_points:
            print("You have tied!")
        else:
            print("You lost!")
    #Ctrl + D is a standard way to exit programs, which is also known as a EOFError

def get_agreement():
    agreement = input("Do you want to play? Type 'yes' or 'no'. ").strip().lower()
    if agreement == "yes":
        return True
    else:
        print("Unfortunately, you don't want to play")
        print("Have a nice day!")
        return False
    #Getting the agreement of the user before the game starts


def rock_paper_scissors(user, computer, userpoints, computerpoints):
    if (
        user == "rock"
        and computer == "scissors"
        or user == "scissors"
        and computer == "paper"
        or user == "paper"
        and computer == "rock"
    ):
        print("You scored one point!")
        userpoints += 1
    elif user == computer:
        print("No points for both sides!")
    else:
        print("The computer scored one point!")
        computerpoints += 1
    return userpoints, computerpoints


main()
# calling main here, so that the program only starts running after this is called.

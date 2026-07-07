import random


def get_user_move():
    print("Pick Rock Paper Scissors")
    return input("Your move: ").lower()


def get_computer_move(moves):
    return random.choice(moves)


def declare_winner(user_move, computer_move):
    if user_move == computer_move:
        print("Draw")
        return "draw"

    elif user_move == "rock":
        if computer_move == "paper":
            print("You lose")
            return "computer"
        else:
            print("You win")
            return "user"

    elif user_move == "paper":
        if computer_move == "scissors":
            print("You lose")
            return "computer"
        else:
            print("You win")
            return "user"

    elif user_move == "scissors":
        if computer_move == "rock":
            print("You lose")
            return "computer"
        else:
            print("You win")
            return "user"


def show_score(user_score, computer_score):
    print(f"Computer: {computer_score}")
    print(f"User: {user_score}")


def show_winner(user_score, computer_score):
    if user_score == 3:
        print("You won the match!")
    elif computer_score == 3:
        print("Computer won the match!")


def main():

    moves = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    user_answer = "y"

    while user_answer == "y":

        user_move = get_user_move()
        computer_move = get_computer_move(moves)

        if user_move not in moves:
            print("Invalid move")
            continue

        print(f"You: {user_move}")
        print(f"Computer: {computer_move}")

        winner = declare_winner(user_move, computer_move)

        if winner == "computer":
            computer_score += 1
        elif winner == "user":
            user_score += 1

        show_score(user_score, computer_score)

        if user_score == 3 or computer_score == 3:
            show_winner(user_score, computer_score)

            user_answer = input("Play again? (y/n): ").lower()

            if user_answer == "y":
                user_score = 0
                computer_score = 0


if __name__ == "__main__":
    main()
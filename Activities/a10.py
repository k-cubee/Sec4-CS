from random import randint


def main():
    play()


def play():
    rand = randint(1, 20)

    # Do while loop for getting number from user until the random number is guessed
    while True:
        num = int(input("Enter a number: "))

        if num == rand:
            print("You are correct")

            # Do while loop for asking whether the user wants to play until they answer yes or no
            while 1 + 1 == 2:
                game = input("Do you want to play another game: ")

                if game.upper() == "NO":
                    break
                elif game.upper() == "YES":

                    # Recursion to play the game again
                    play()
                    break
            break
        elif num < 1 or num > 20:
            print("Your number must be between 1 and 20")
        elif num < rand:
            print("Your number is too small")
        else:
            print("Your number is too high")


main()

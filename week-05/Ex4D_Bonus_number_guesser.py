number_pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mixed_numbers = set(number_pool)

secret_number = mixed_numbers.pop()

guess_history = []
guess_count = 0
correct_guess = False

print("Guess the number between 1 and 10.")

while correct_guess == False:
    user_input = input("Enter your guess: ")

    if user_input.isdigit() == False:
        print("Please enter a valid number.")
    else:
        guess = int(user_input)

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        else:
            guess_count = guess_count + 1
            guess_history.append(guess)

            if guess < secret_number:
                print("Higher")
            elif guess > secret_number:
                print("Lower")
            else:
                print("You got it!")
                print("Number of guesses:", guess_count)
                print("Your guesses were:", guess_history)

                if guess_count < 5:
                    print("Awesome job!")

                correct_guess = True

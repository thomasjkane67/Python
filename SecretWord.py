# Guess my secret word
secret_word = "giraffe"
guess = ""
guess_count = 0

print("You have 3 guesses")

while guess_count < 3 and guess != secret_word:
    if guess_count == 0:
        hint = "It lives in Africa: "
    elif guess_count == 1:
          hint = "It has tan spots: "
    elif guess_count == 2:
        hint = "It has a long neck: "

    guess = raw_input(hint)
    guess_count += 1

    if guess == secret_word:
        print("You win! ")
    else:
        print("Guess again: ")

if guess != secret_word:
    print("Sorry you lost! ")

# more efficient
secret_word = "hippopotamus"
guess = ""
guess_count = 0
guess_limit = 3
out_of_Guesses = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guesses:
    print("Out of guesses, you lose! ")
else:
    print("you win! ")
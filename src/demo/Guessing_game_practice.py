secret_word = "cat"
guess = ""
tries = 0
tries_limit = 5
out_of_tries = False

while guess != secret_word and not(out_of_tries):
    if tries < tries_limit:
        tries_remaining = tries_limit - tries
        guess = input("Guess an animal (" + str(tries_remaining) + " guess(es) left): ")
        tries += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("You lose!")
    print("Answer: cat")
else:
    print("You win!")
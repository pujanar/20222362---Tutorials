
hidden_number = random.randint(1, 20)
print("Random hidden number is:", hidden)

while True:
    guess = int(input("Enter a guess (between 1 and 20): "))
    if guess == hidden:
        print("uess is correct.")
        break
    elif guess < hidden:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

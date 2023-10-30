
hidden_Number = random.randint(1, 20)
print("Random hidden number is:", hidden_number)

while True:
    guess = int(input("Enter a guess (between 1 and 20): "))
    if guess == hidden_number:
        print("Guess is correct.")
        break

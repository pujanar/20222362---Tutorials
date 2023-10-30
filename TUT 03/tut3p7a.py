import random
secret_number = input("Enter to flip the coin:")
secret_number = random.randint(0,1)

if secret_number == 0 :
    print("Heads")

else:
    print("Tails")

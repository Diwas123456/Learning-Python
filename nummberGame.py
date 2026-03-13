import random
secret_number = random.randint(1, 100);
guess = int(input("Guess the number between 1 and 100: "))
while guess != secret_number:
    if guess < secret_number:
        print("Low! Try again.")
    else:
        print("High! Try again.")
    guess = int(input("Guess the number between 1 and 100: "))  
print("Congratulations! You guessed the number.")
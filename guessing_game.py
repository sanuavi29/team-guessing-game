import random

while True:
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")
    guess = int(input())
<<<<<<< HEAD
    if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")

=======
>>>>>>> 2d6626e93bc57317d1aeb5cc681339ec9bea3f5a
    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")
    
    print("Play again? (y/n)")
    if input().lower() != 'y':
<<<<<<< HEAD
        break
=======
        break
>>>>>>> 2d6626e93bc57317d1aeb5cc681339ec9bea3f5a

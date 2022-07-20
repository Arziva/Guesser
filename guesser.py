import random

def guess(x):
    random_no = random.randint(0,x)
    guess = 0
    while(guess != random_no):
        guess = int(input(f"Enter a guess between 1 and {x}:"))
        if guess > random_no:
            print("Sorry, guess is too high")
        elif guess < random_no:
            print("Sorry, guess is too low")
    print(f"Awesome, you have guessed the number {random_no}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while(feedback != 'c'):
        if(low!=high):
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"The guess is correct!")


computer_guess(10)
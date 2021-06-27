import random
# Importing random so that it will genrate a random number each time we run this file
random_number = random.randint(1,100) # it will generate a random number between 1 and 100 and can even be 1 or 100
points = 100 # Points user has gained, it will reduce as the number of guesses increase
guessed_num = 0 # The guessed number user inputed it will initially be 0 so that the random number and guessed number will not be same
tries = 0 # number of tries user took to guess the number
run = True
while run:
    guessed_num = input("Enter your guess (1-100): ") # it will take a number in string from the user
    try:
        int(guessed_num) # if guessed number can be converted into an integer we are good to go ortherwise it will go to the except block
        tries += 1 # every time user guess a number it will increase the tries by 1 and lessen the points by 10 each time
        if int(guessed_num) > random_number: # if guessed number is more than random number
            print("Too High")
            points -=10
        elif int(guessed_num) < random_number: # if guessed number is less than random number
            print("Too Low")
            points -=10
        else: # if the guessed number is neither more nor less it must be the random number
            run = False
    except ValueError: # if the number is not an integer it will genrate a value error
        print("Please enter a integer")
    except:
        print("Unexpected error") # for an unexpected error so that program won't directly crash
       

print(f"Congratulaions, you guessed the number in {tries} Tries.\nYour score is {points}") # if the user guess the random number this will be printed

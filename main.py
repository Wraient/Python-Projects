import random
random_number = random.randint(1,100)
points = 100
guessed_num = 0
tryies = 0
run = True
while run:
    guessed_num = input("Enter your guess (1-100): ")
    try:
        int(guessed_num)
        tryies += 1
        print(tryies)
        if int(guessed_num) > random_number:
            print("Too High")
            points -=10
        elif int(guessed_num) < random_number:
            print("Too Low")
            points -=10
        else:
            run = False
    except ValueError:
        print("Please enter a integer")
    
print(f"Congratulaions, you guessed the number in {tryies} Tries.\nYour score is {points}")
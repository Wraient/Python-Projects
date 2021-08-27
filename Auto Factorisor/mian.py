import os
import time
# def EnterNum(mainFunc):
#     print("Please enter a number")

def mainFunc():
    # Uncomment below lines for knowing the time needed for the program (a bit of bug will fix it later...)
    # t1 = time.time()
    try:
        os.system("clear")
        additional  = int(input("Enter the middle number : "))
        multiplier = int(input("Enter the last number : "))
        run = True
        found = False
    # Not very efficient but works fine for me (time and space complexity of O^2 or more I guess)
        for i in range(1, 1000):
            if found == True:break
            if run == False:break
            for j in range(1, 1000):
                if i*j==multiplier:
                    if i+j==additional or i-j==additional or j-i==additional:
                        print(f"The answer is {i} and {j}" )
                        found = True
                        run = False
        if found == False:
            print("\nno solution between 1 and 1000")
    except ValueError:
        num = False
        mainFunc()
    # t2 = time.time()
    # print("\nTime : " + str(t2-t1) + " ms")

mainFunc()
while True:
	cmd = input("\nPress \"n\" to do other calculation and any other key to quit ")
	if cmd.lower() == "n":
		mainFunc()
	else:
		break

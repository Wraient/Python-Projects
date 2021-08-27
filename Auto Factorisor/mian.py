import os
import time

def mainFunc():
    def isInt(string):
        try:
            int(string)
            return True
        except:
            return False

    num = True
    while True:
        # Uncomment below lines for knowing the time needed for the program 
        # t1 = time.time()
        try:
            os.system("clear")
            if num == False:
                print("Please enter a number.")
                num = True
            additional  = int(input("Enter the middle number : "))
            try:
                os.system("clear")
                print("Middle number : " + str(additional))
                multiplier = int(input("Enter the product of first and last number : "))
            except ValueError:
                while True:
                    os.system("clear")
                    print("Please enter a number")
                    print("\nMiddle number : " + str(additional))
                    multiplier = input("Enter the product of first and last number : ")
                    if isInt(multiplier):
                        multiplier = int(multiplier)
                        break
            run = True
            found = False
        # Not very efficient but works fine for me (time and space complexity of O^2 or more I guess)
            for i in range(-1, 1000):
                if found == True:break
                if run == False:break
                for j in range(-1, 1000):
                    if i*j==multiplier:
                        if i+j==additional or i-j==additional or j-i==additional:
                            print(f"The answer is {i} and {j}" )
                            found = True
                            run = False
            if found == False:
                print("\nno solution between 0 and 1000.")
            
            # t2 = time.time()
            # print("\nTime : " + str(t2-t1) + " seconds")
            cmd = input("\nPress \"n\" to do other calculation and any other key to quit ")
            if cmd.lower() == "n": continue
            else:
                os.system("clear")
                break

        except ValueError:
            num = False


mainFunc()

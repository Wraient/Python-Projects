import os
import time
time_Used = time.time()
def mainFunc():
    def isInt(string):
        try:
            int(string)
            return True
        except:
            return False

    num = True
    while True:
        # comment below appropriate lines for hiding the time used by the program
        t1 = time.time()
        try:
            os.system("clear")
            if num == False:
                print("Please enter a number.")
                num = True
            t2 = time.time()
            additional  = int(input("Enter the middle number : "))
            t3 = time.time()
            t4 = 0
            try:
                os.system("clear")
                print("Middle number : " + str(additional))
                t4 = time.time()
                multiplier = input("Enter the product of first and last number : ")
                t5 = time.time()
                multiplier = int(multiplier)
                t6 = time.time()
                time_taken_by_computer = (t2-t1)+(t4-t3)+(t6-t5)
                time_taken_by_user = (t3-t2)+(t5-t4)
            except ValueError:
                t6 = time.time()
                time_taken_by_computer = (t2-t1)+(t4-t3)+(t6-t5)
                time_taken_by_user = (t5-t4)+(t3-t2)
                t6 = 0
                while True:
                    os.system("clear")
                    print("Please enter a number")
                    print("\nMiddle number : " + str(additional))
                    if t6 == 0:
                        t6 = time.time()
                    multiplier = input("Enter the product of first and last number : ")
                    t7 = time.time()
                    if isInt(multiplier):
                        multiplier = int(multiplier)
                        

                        time_taken_by_computer = (t2-t1)+(t4-t3)+(t6-t5)
                        time_taken_by_user = (t5-t4)+(t3-t2)+(t7-t6)
                        break
            os.system("clear")
            print("Middle number : " + str(additional))
            print("Last number : " + str(multiplier) + "\n")
            t8 = time.time()
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
            
            t9 = time.time()
            print(f"\nTime taken by user : {str(round(time_taken_by_user, 4))} seconds\nTime taken by CPU : {str(round(time_taken_by_computer+(t9-t8), 4))} seconds")
            cmd = input("\nPress \"n\" to do other calculation and any other key to quit : ")
            if cmd.lower() == "n": continue
            else:
                os.system("clear")
                time_Used2 = time.time()
                print("Used application for : " + str(time_Used2 - time_Used) + " seconds")
                cmd1 = input("\nPress \"n\" to do other calculation and any other key to quit : ")
                if cmd1.lower() == "n": continue
                else: break

        except ValueError:
            num = False


mainFunc()

import time
print ("Welcome to the python calculator program!")
time.sleep(0.9)
print ("With this program you can use the calculator as many times as you want.")
time.sleep(0.5)
Use=str(input("Do you want to use the calculator? (Yes/No) "))
if Use=="No":
    quit()
else:
    First_number=int(input("Enter the first number - "))
    Second_number=int(input("Enter the second number - "))
    print ("There are 4 operations this program can do for you: ")
    time.sleep(0.7)
    print ("1. Addition")
    time.sleep(0.7)
    print ("2. Subtraction")
    time.sleep(0.7)
    print ("3. Multiplication")
    time.sleep(0.7)
    print ("4. Division")
    time.sleep(0.7)
    Operation=int(input("Enter the operation you want to do (1/2/3/4) - "))
    if Operation==1:
        print ("The addition is " ,First_number+Second_number)
    if Operation==2:
        print ("The subtraction is " ,First_number+Second_number)
    if Operation==3:
        print ("The multiplication is " ,First_number*Second_number)
    if Operation==4:
        print ("The division is " ,First_number/Second_number)
while True:
    Again=str(input("Do you want to use the calculator again for the same numbers or for different numbers? (Yes/No) "))
    if Again=="No":
        print ("Thanks for using this program!")    
        quit() 
    else: 
        New_numbers=str(input("Do you want to use different numbers this time? (Yes/No) "))
        if New_numbers=="No":
            Operation=int(input("Enter the operation you want to do (1/2/3/4) - "))
            if Operation==1:
                print ("The addition is " ,First_number+Second_number)
            if Operation==2:
                print ("The subtraction is " ,First_number+Second_number)
            if Operation==3:
                print ("The multiplication is " ,First_number*Second_number)
            if Operation==4:
                print ("The division is " ,First_number/Second_number)
        else:
            First_number=int(input("Enter the first number - "))
            Second_number=int(input("Enter the second number - "))
            print ("There are 4 operations this program can do for you: ")
            time.sleep(0.7)
            print ("1. Addition")
            time.sleep(0.7)
            print ("2. Subtraction")
            time.sleep(0.7)
            print ("3. Multiplication")
            time.sleep(0.7)
            print ("4. Division")
            time.sleep(0.7)
            Operation=int(input("Enter the operation you want to do (1/2/3/4) - "))
            if Operation==1:
                print ("The addition is " ,First_number+Second_number)
            if Operation==2:
                print ("The subtraction is " ,First_number+Second_number)
            if Operation==3:
                print ("The multiplication is " ,First_number*Second_number)
            if Operation==4:
                print ("The division is " ,First_number/Second_number)

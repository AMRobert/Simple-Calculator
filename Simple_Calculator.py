#SIMPLE CALCULATOR

#Function for addition
def addition(num1,num2):
    return num1 + num2

#Function for subtraction
def subtraction(num1,num2):
    return num1 - num2

#Function for multiplication
def multiplication(num1,num2):
    return num1 * num2

#Function for division
def division(num1,num2):
    return num1 / num2


#Function for Calculation
def calc():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter your choice: "))
    


    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Addition of",int(num1),"and",int(num2),"=",addition(num1,num2))
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Subtraction of",num1,"and",num2,"=",subtraction(num1,num2))
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Multiplication of",num1,"and",num2,"=",multiplication(num1,num2))
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Division of",num1,"and",num2,"=",division(num1,num2))
    else:
        print("Invalid Input")
        print("Please choose the correct options")
        calc()


print("SIMPLE CALCULATOR")
print("Choose which operation you want to do!..")
calc()

for i in range(100):
    print("<------------------------>")
    print("Do you want to continue!..")
    print("1.yes")
    print("2.No")
    second_choice = int(input("Enter your choice: "))
    if second_choice==1:
        calc()
    else:
        print("Thank You")
        exit()



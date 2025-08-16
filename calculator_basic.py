print("--------------CALCULATOR--------------")
print("Enter 1 for Addition \n Enter 2 for Subtraction \n Enter 3 for Multiplication \n Enter 4 for Division \n")

op = int(input("Enter operation number you would like to perform : "))
print(" ")

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
print(" ")

if(op == 1):
    print("Sum of Two numbers is : ",(num1 + num2))
elif(op == 2):
    print("Difference between two numbers is : ",(num1 - num2))
elif(op == 3):
    print("Product of Two numbers is : ",(num1 * num2))
elif(op == 4):
    print("Dividing first number with second gives ",(num1 / num2))
else:
    print(f"{op} is not a valid operator")






print("----------------- WEIGHT CONVERTER -----------------")
print("Enter 1 to convert from Kgs to Pounds \n Enter 2 to convert Pounds to Kgs \n")

op = int(input("Enter operation number : "))

if(op == 1):
    weight = float(input("Enter your weight in Kgs : "))
    print("Your Weight in Pounds is ",weight*2.20462262)
elif(op == 2):
    weight = float(input("Enter your weight in Pounds : "))
    print("Your Weight in Kgs is ",(weight/2.20462262))
else:
    print("Enter Valid Operation")
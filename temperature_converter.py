print("---------TEMPERATURE CONVERTER----------")
print("Enter 1 to Convert Celsius to Fahrenheit \n Enter 2 to Convert Fahrenheit to Celsius \n")

op = int(input("Enter operation number : "))
print(" ")

if(op == 1):
    c = float(input("Enter Temperature in Celsius : "))
    print("Temperature in Fahrenheit is ",(c*1.8)+32)
elif(op == 2):
    f = float(input("Enter Temperature in Fahrenheit : "))
    print("Temperature in Celsius ",((f-32)/1.8))
else:
    print("Enter Valid Operation")
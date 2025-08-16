item = input("Enter item you want to purchase : ")
price = float(input("Enter price of item in rupees : "))
quant = int(input("Enter quantity of item you want to purchase : "))

total = price*quant

print("\nYou are buying",quant,item)
print("The total cost of purchase is ",total," rupees")



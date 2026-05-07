#Define known values 
food_cost = 79.25
tax = 6.54
tip = 12.00
#calculate the unknown

total_due = food_cost + tax + tip
print("The total due is " + str(total_due)) # the str function is used to cast data types here its changing the integer to a string>

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Total due is "+ str(total_due) )
print("Tip is " + format(tip, ".2f"))
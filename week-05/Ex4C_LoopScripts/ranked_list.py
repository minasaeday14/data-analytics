favorite_foods = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

for index, item in enumerate(favorite_foods, start=1):
    if index == 1:
        print(index, ".", item, " <- top pick!", sep="")
    else:
        print(index, ".", item, sep="")

#Bonus - in reversed order
print("Bonus - using reversed() to print list in reverse order")
for index, item in enumerate(reversed(favorite_foods), start=1):
    if index == 1:
        print(index, ".", item, " <- top pick!", sep="")
    else:
        print(index, ".", item, sep="")

a = 12
b = 7
c = 20

if a <= b and a <= c:
    smallest = a
else:
    if b <= a and b <= c:
        smallest = b
    else:
        smallest = c

if a >= b and a >= c:
    largest = a
else:
    if b >= a and b >= c:
        largest = b
    else:
        largest = c

print("The smallest number is", smallest)
print("The largest number is", largest)

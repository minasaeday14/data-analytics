# Description: This script tests various numeric conversion techniques
# Author: Mina Saeday

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


# a_int = int(a)  
# # ValueError: invalid literal for int() with base 10: ' 101.1 '

b_int = int(b)

# c_int = int(c)
# ValueError: invalid literal for int() with base 10: '402 Stevens'

# d_int = int(d)  
# ValueError: invalid literal for int() with base 10: 'Number 5 '

a_float = float(a)

b_float = float(b)

# c_float = float(c) 
# ValueError: could not convert string to float: '402 Stevens'

# d_float = float(d)  
# ValueError: could not convert string to float: 'Number 5 '

a_float_int = int(float(a))

b_float_int = int(float(b))

# c_float_int = int(float(c))
# ValueError: could not convert string to float: '402 Stevens'

# d_float_int = int(float(d))
# ValueError: could not convert string to float: 'Number 5 '

a_slice = a[1:6]
b_slice = b[:]
c_slice = c[0:3]
d_slice = d[7:8]

a_slice_float = float(a_slice)
b_slice_int = int(b_slice)
c_slice_int = int(c_slice)
d_slice_int = int(d_slice)

#Printing out the results

print(a_float)
print(b_int)
print(b_float)
print(a_float_int)
print(b_float_int)

print(a_slice)
print(b_slice)
print(c_slice)
print(d_slice)

print(a_slice_float)
print(b_slice_int)
print(c_slice_int)
print(d_slice_int)

print(a.strip())
print(d.strip())
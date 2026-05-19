#Value error
try:
    num = int("hello")
except ValueError:
    print("Value Error: You tried to convert a text into a number.")
else: 
    print(num)
finally:
    print("Lets try another one...\n")


#Name error
try:
    m = "banana"
except NameError:
    print("NameError:You used a variable thats not defined.")
else:
    print(m)
finally:
    print("Lets try another one...\n")


#Type error
try:
    result = "2" + 2
except TypeError:
    print("Type Error: You tried to use two incompatible data types together.")
else:
    print(result)
finally:
     print("Lets try another one...\n")


#Syntax Error
try: 
    exec("if True print('hello')")
except SyntaxError:
    print("Syntax Error: There is something wrong with the way the coode is written")
else:
    print("No syntax error found")
finally:
     print("Lets try another one...\n")   
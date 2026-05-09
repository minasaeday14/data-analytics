department_code = 12

match department_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code")

# My classmates approached the solution similarly. 
# Both match and if statments are easy to understand and do the same thing.
# I woultn't change anything from my implementation, apart from one thing - i wish i could test for multiple departments at once without manually changing them

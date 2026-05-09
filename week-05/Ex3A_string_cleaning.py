# Description: This script tests various string conversion techniques
# Author: Mina Saeday

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1_lowercase = name_1.lower()
name_2_lowercase = name_2.lower()
name_3_lowercase = name_3.lower()

print(name_1_lowercase)
print(name_2_lowercase)
print(name_3_lowercase)

name_1_title = name_1.title()
name_2_title = name_2.title()
name_3_title = name_3.title()

print(name_1_title)
print(name_2_title)
print(name_3_title)

salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")

print(salary_1_no_dollar, type(salary_1_no_dollar))
print(salary_2_no_dollar, type(salary_2_no_dollar))

# To perform math, you would also need to remove the comma and convert to int

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int, type(salary_1_int))
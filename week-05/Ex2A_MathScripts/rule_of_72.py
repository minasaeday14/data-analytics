current_savings = 3000
interest_rate = 0.06
interest_rate_whole = 6

doubled_balance = current_savings * 2
years = 72/interest_rate_whole

print("Your current savings is", current_savings)
print("At a", format(interest_rate, ".0%"), "interest rate, your savings account will be worth", format(doubled_balance, ".2f"), "in", format(years, ".1f"),"years" )
pay_rate = 17.30
hours_worked = 45
filing_status = "single"

if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

annual_gross_income = gross_pay * 52

if filing_status == "single":
    if annual_gross_income < 12000:
        tax_rate = 0.05
    elif annual_gross_income < 25000:
        tax_rate = 0.10
    elif annual_gross_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_gross_income < 12000:
        tax_rate = 0.00
    elif annual_gross_income < 25000:
        tax_rate = 0.06
    elif annual_gross_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    print("Invalid filing status")
    tax_rate = 0

tax_withholding = gross_pay * tax_rate
net_pay = gross_pay - tax_withholding

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your annual gross income is ${annual_gross_income:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withholding:.2f}")
print(f"Your net pay is ${net_pay:.2f}")
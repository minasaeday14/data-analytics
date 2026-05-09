pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked

print(f"Pay rate: ${pay_rate:>2f}")
print(f"Hours worked: {hours_worked}")
print(f"Gross pay: ${gross_pay:.2f}")
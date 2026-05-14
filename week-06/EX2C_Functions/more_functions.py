def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(city + ", " + state + " " + zip_code)


def add_numbers(*numbers):
    total = 0
    result_text = ""

    for i in range(len(numbers)):
        total = total + numbers[i]

        if i == 0:
            result_text = str(numbers[i])
        else:
            result_text = result_text + " + " + str(numbers[i])

    print(result_text + " = " + str(total))


def display_receipt(total_due, amount_paid):
    print("Total Due: $" + str(total_due))
    print("Amount Paid: $" + str(amount_paid))

    if amount_paid > total_due:
        change_due = amount_paid - total_due
        print("Change Due: $" + str(change_due))
    elif amount_paid == total_due:
        print("Change Due: $0")
    else:
        balance_due = total_due - amount_paid
        print("Remaining Balance: $" + str(balance_due))


display_mailing_label("Mina Saeday", "161 Brickrow", "Richardson", "TX", "75081")
print("\n")
display_mailing_label("Eyerusalem Debero", "76 Forest Lane", "Richardson", "TX", "75082")

print("\n")
add_numbers(5)
add_numbers(5, 10)
add_numbers(1, 2, 3, 4, 5)

print("\n")
display_receipt(20, 25)
print("\n")
display_receipt(30, 30)
print("\n")
display_receipt(20, 15)
e
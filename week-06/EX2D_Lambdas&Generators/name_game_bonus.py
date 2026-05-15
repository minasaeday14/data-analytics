def name_game(name):
    name = name.strip().title()

    first_name = name.split()[0]

    if len(first_name) > 1:
        short_name = first_name[1:]
    else:
        short_name = first_name

    return f"{first_name}, {first_name}, bo-B{short_name}\nBanana-fana fo-F{short_name}\nFee-fi-mo-M{short_name}\n{first_name}!"


names = ["Nura", "Lena", "Omar", "Osman", "Sebrin"]

for name in names:
    print(name_game(name))
    print()


# Observation: this version handles uppercase and lowercase names better, but names starting with b, f, or m may need special rules.

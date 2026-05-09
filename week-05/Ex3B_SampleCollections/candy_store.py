candy_types = ("gummy rings", "lollipops", "jelly beans")
fruity_flavors = ("strawberry", "green apple", "blue raspberry")

candy_combinations = set()

candy_combinations.add(fruity_flavors[0] + " " + candy_types[2])
candy_combinations.add(fruity_flavors[1] + " " + candy_types[1])
candy_combinations.add(fruity_flavors[2] + " " + candy_types[0])

print("Today's candy options include:", candy_combinations)
print("Today's candy options include:", candy_combinations)
print("Today's candy options include:", candy_combinations)

# It looks like the set is unordered, so the combination is not in the order that was inputed

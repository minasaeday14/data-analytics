import math

people = 38
seats_per_van = 15
cost_per_van = 250

vans_needed = math.ceil(people / seats_per_van)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / people

print("Vans needed:", vans_needed)
print("Total van cost:", total_cost)
print("Cost per person:", round(cost_per_person, 2))
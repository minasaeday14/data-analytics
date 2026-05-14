import random
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']
product_of_the_day = random.choice(products)
print("Product of the day:", product_of_the_day)
survey_products = random.sample(products,3)
print("Survey Products:", survey_products)

random.shuffle(products)
print("Shuffled Products:", products)

transaction_count = random.randint(50, 300)
print("Daily transaction count:", transaction_count)
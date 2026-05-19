class Restaurant:
    """This class represents a restaurant and keeps track of food type, customers served, and customer ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, num):
        self.number_served += num

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            average = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {average:.2f}")
        else:
            print("Invalid rating. Please enter an integer from 1 to 5.")





rest1 = Restaurant("Yemandi", "Yemeni food")
rest2 = Restaurant("Desta", "Ethiopian food")
rest3 = Restaurant("Dunkin Dunnts", "donuts and coffee")

rest1.print_num_served()
rest1.add_num_served(20)
rest1.add_num_served(15)
rest1.print_num_served()

print()

rest2.print_num_served()
rest2.add_num_served(10)
rest2.add_num_served(30)
rest2.print_num_served()

print()

rest3.print_num_served()
rest3.add_num_served(40)
rest3.add_num_served(25)
rest3.print_num_served()


rest1.customer_rating(5)
rest1.customer_rating(4)
rest1.customer_rating(3)

print()

rest2.customer_rating(4)
rest2.customer_rating(5)
rest2.customer_rating(5)

print()

rest3.customer_rating(2)
rest3.customer_rating(3)
rest3.customer_rating(4)

rest1.customer_rating(5)
rest1.customer_rating(4)
rest1.customer_rating(3)

print()

rest2.customer_rating(4)
rest2.customer_rating(5)
rest2.customer_rating(5)

print()

rest3.customer_rating(2)
rest3.customer_rating(3)
rest3.customer_rating(4)

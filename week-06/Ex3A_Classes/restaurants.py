class Restaurant:
    """This class represents a restaurant and stores its name and food type."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
         print(f"{self.rest_name} is open.")


rest1 = Restaurant("Yemandi", "Yemeni food")
rest2 = Restaurant("Desta", "Ethiopian food")
rest3 = Restaurant("Dunkin Dunnts", "donuts and coffee")


rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()


        
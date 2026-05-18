cust_list = []


class RewardsProgram:
    """This class stores customer contact information for a restaurant rewards program."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


cust1 = RewardsProgram("Mina Saeday", "214-555-1111", "mina@email.com")
cust2 = RewardsProgram("Eyerusalem Debero", "214-555-2222", "eyerusalem@email.com")
cust3 = RewardsProgram("Nura Ali", "214-555-3333", "nura@email.com")

cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()

print()

cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()

print()

cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

print()
print(cust_list)

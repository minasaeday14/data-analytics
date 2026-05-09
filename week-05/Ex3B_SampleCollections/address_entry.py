contact_info = {
    "name": "Mina Saeday",
    "address": "123 Main Street",
    "city": "Richardson",
    "state": "TX",
    "zip": "75081"
}

print(f"""Mina Saeday
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

contact_info.pop("name")

full_name = {
    "first name": "Mina",
    "last name": "Saeday"
}

full_name.update({"honorific": "Ms."})

contact_info.update({"full_name": full_name})

print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

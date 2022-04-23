import random


class SecretSanta:
    def __init__(self):
        self.membersData = []
        self.membersName = []

    def get_members_names(self):
        users = input("Enter Users seperated by (,): ")
        if len(users.split(',')) < 4:
            users = input("Enter at least 4 Users")
            return False
        self.membersName = users.split(",")
        self.membersName = [name.strip() for name in self.membersName]
        self.get_members_data()
        self.get_random_choice()

    def get_members_data(self):
        for name in self.membersName:
            data = {"name": name, "assigned": False, "partner": ""}
            self.membersData.append(data)

    def get_random_choice(self):
        while True:
            member = random.choice(self.membersName)
            partner = random.choice(self.membersName)
            if member != partner:
                for this in self.membersData:
                    if this["name"] == member and not this["assigned"]:
                        if not any(d["partner"] == partner
                                   for d in self.membersData):
                            this["assigned"] = True
                            this["partner"] = partner

            if all(this["assigned"] == True for this in self.membersData):
                break

        for data in self.membersData:
            print(data["name"], " is assigned to ", data["partner"])


if __name__ == '__main__':
    ss = SecretSanta()
    ss.get_members_names()

import json

class AccountManager:
    def __init__(self):
        self.users = []

    def print_users(self):
        self.load_users()
        for user in self.users:
            print(user)

    def load_users(self):
        with open('users.json', 'r') as file:
            users = json.load(file)
            users = users["users"]

        return users
    
    def login(self, first_name, last_name, password):
        users = self.load_users()
        for user in users:
            if user["first_name"] == first_name.capitalize() and user["last_name"] == last_name.capitalize() and user["password"] == password:
                return user
        
        raise Exception("Invalid credentials")

    def register_user(self, first_name, last_name):
        users = self.load_users()

        user = {
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "password" : last_name.capitalize(),
            "balance" : 0.0,
            "id" : len(users) + 1
        }

        
        users.append(user)

        with open('users.json', 'w') as file:
            json.dump({"users": users}, file, indent=4)

    def lodge_funds(self, id, amount):
        users = self.load_users()
        
        with open('users.json', 'w') as file:
            for user in users:
                if user["id"] == id:
                    user["balance"] += amount
                    json.dump({"users": users}, file, indent=4)
                    return user["balance"]
                
    def withdraw(self, id, amount):
        users = self.load_users()
        
        with open('users.json', 'w') as file:
            for user in users:
                if user["id"] == id:
                    if user["balance"] < amount:
                        json.dump({"users": users}, file, indent=4)
                        raise Exception("Not enough funds")
                    
                    user["balance"] -= amount
                    json.dump({"users": users}, file, indent=4)
                    return user["balance"]
                
    def change_password(self, id, old_password, new_password):
        users = self.load_users()
        
        with open('users.json', 'w') as file:
            for user in users:
                if user["id"] == id:
                    if user["password"] != old_password:
                        json.dump({"users": users}, file, indent=4)
                        raise Exception("Invalid password")
                    
                    user["password"] = new_password

                    json.dump({"users": users}, file, indent=4)
                    return True
                
    def calculate_interest(self, id, months=12):
        users = self.load_users()

        for user in users:
            if user["id"] == id:
                principal = user["balance"]
                break

        monthly_interest = []  
        monthly_percent = []

        for month in range(1, months + 1):
            if principal < 5000:
                rate = 0.02  
            else:
                rate = 0.04 

            interest = (principal * rate) / 12 
            principal += interest 
            monthly_percent.append(rate)
            monthly_interest.append(round(interest, 2))  

        return monthly_percent, monthly_interest

        
        
    



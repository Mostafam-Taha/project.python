# Admin or User\
import os
import json

file_system = "Account_user.json"
def load_data():
    if not os.path.exists(file_system):
        return[]
    with open(file_system, "r", encoding="utf-8") as file_as_creat_account:
        return json.load(file_as_creat_account)

def save_data(data):
    with open(file_system, "w", encoding="utf-8") as file_as_creat_account:
        json.dump(data, file_as_creat_account, ensure_ascii=False, indent=4)

class Account_Manager:
    def __init__(self, option_user_or_admin):
        self.option_user_or_admin = option_user_or_admin

    def admin_or_user(self):
        if self.option_user_or_admin == "admin":
            pass
        elif self.option_user_or_admin == "user":
            self.account_user()
        else:
            print("Error")

    def account_user(self):
        data = load_data()
    
        print("="* 20)
        print("Welcome to User")
        print("="* 20)

        username = input("Please enter your username: ")
        while True:
            password = input("Please ente your password: ")
            currunt_password = input("Please enter your currunt password: ")
            if password == currunt_password:
                print("Done: created account success")
                break
            else:
                print("Error: Faild")
                continue

        new_id = max([emp["ID"] for emp in data], default=0) + 1
        data_user = {
            "id": new_id,
            "Type Account": "User",
            "Username": username,
            "Password": password
        }

        data.append(data_user)
        save_data(data)

op_us_ad = input("Your admin or user: ")
Account_Manager(op_us_ad).admin_or_user()

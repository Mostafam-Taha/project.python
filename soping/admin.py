import os
import json
# import main
from datetime import datetime

data_products = "data_product.json"
data_admin_return = "Account_user.json"

def load_data():
    if not os.path.exists(data_products):
        return[]
    with open(data_products, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(data_products, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def sgin_up_admin():
    # data = main.load_data()
    print("=" *20)
    print("Welcom to Admin")
    print("=" *20)
    while True:
        try:
            username = input("Please enter your username: ").strip()
            break
        except ValueError:
            print("Error: Please enter your username currect")
            continue
    while True:
        try:
            password_admin = input("Please enter your password: ").strip()
            password_currunt = input("Please enter your password Currunt: ").strip()
            if password_admin == password_currunt:
                break
            else:
                continue
        except ValueError:
            continue

    # new_id = max([id["id"] for id in data], default=0) + 1
    created_at = datetime.now().strftime("%b-%y-%d %H:%M:%S")
    new_account_admin = {
        # "id": new_id,
        "Type Account": "Admin",
        "Username": username,
        "Password": password_admin,
        "Created_at": created_at
    }

    # data.append(new_account_admin)
    # main.save_data(data)

def login_admin():
    # while True:
    #     try:
    #         username = input("Please enter your username: ").strip()
    #         break
    #     except ValueError:
    #         print("Error: Please enter your username")
    #         continue
    pass

def add_product():
    data = load_data()
    while True:
        try:
            name_product = input("Please enter your name product: ").strip()
            break
        except ValueError:
            print("Error: Please enter your name product is currect")
            continue
    while True:
        try:
            price_product = int(input(f"Please enter your price {name_product}: "))
            break
        except ValueError:
            print("Error: Please enter your price is currect")
            continue
    while True:
        try:
            qauntity_product = int(input(f"Please enter your qountity {name_product}:"))
            break
        except ValueError:
            print("Error: Please enter your qauntity is currect")
            continue
    created_at = datetime.now().strftime("%b-%y-%d %H:%M:%S")

    new_id = max([emp["id"] for emp in data], default=0) + 1
    new_product = {
        "id": new_id,
        "Name Product": name_product,
        "Price Product": price_product,
        "Qauntity Product": qauntity_product,
        "Created_at": created_at
    }

    data.append(new_product)
    save_data(data)


s = input("username: ")
with open(data_admin_return, "r", encoding="utf-8") as f:
    data = json.load(f)
    new_account = []
    for i in data: 
        if (i.get("Type Account") == "User" or "Admin") and i["Username"] != s:
            new_account.append(i)
            print("done")

    print(new_account)
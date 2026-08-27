import os
import json
from datetime import datetime

data_products = "data_product.json"

def load_file():
    if not os.path.exists(data_products):
        return[]
    with open(data_products, "r", encoding="utf-8") as f:
        return json.load(f)

def save_file(data):
    with open(data_products, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_product():
    data = load_file()
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
    save_file(data)

add_product()
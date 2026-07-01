def find_top_seller(products: dict, sales: dict) -> str:
    return max(products, key=lambda nomi: products[nomi] * sales[nomi])


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))
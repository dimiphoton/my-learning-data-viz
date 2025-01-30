import pandas as pd
import random
from datetime import datetime, timedelta

# Liste de pays de l'UE et leurs villes avec coordonnées
eu_cities = [
    {"country": "France", "cities": [("Paris", 48.8566, 2.3522), ("Lyon", 45.7640, 4.8357), ("Marseille", 43.2965, 5.3698)]},
    {"country": "Germany", "cities": [("Berlin", 52.5200, 13.4050), ("Munich", 48.1351, 11.5820), ("Hamburg", 53.5511, 9.9937)]},
    {"country": "Italy", "cities": [("Rome", 41.9028, 12.4964), ("Milan", 45.4642, 9.1900), ("Naples", 40.8518, 14.2681)]},
    {"country": "Spain", "cities": [("Madrid", 40.4168, -3.7038), ("Barcelona", 41.3851, 2.1734), ("Valencia", 39.4699, -0.3763)]},
    {"country": "Netherlands", "cities": [("Amsterdam", 52.3676, 4.9041), ("Rotterdam", 51.9225, 4.4792), ("The Hague", 52.0705, 4.3007)]},
    {"country": "Belgium", "cities": [("Brussels", 50.8503, 4.3517), ("Antwerp", 51.2194, 4.4025), ("Ghent", 51.0543, 3.7174)]},
    {"country": "Poland", "cities": [("Warsaw", 52.2297, 21.0122), ("Krakow", 50.0647, 19.9450), ("Wroclaw", 51.1079, 17.0385)]},
    {"country": "Portugal", "cities": [("Lisbon", 38.7169, -9.1399), ("Porto", 41.1579, -8.6291), ("Coimbra", 40.2033, -8.4103)]},
    {"country": "Sweden", "cities": [("Stockholm", 59.3293, 18.0686), ("Gothenburg", 57.7089, 11.9746), ("Malmo", 55.6049, 13.0038)]},
    {"country": "Austria", "cities": [("Vienna", 48.2082, 16.3738), ("Graz", 47.0707, 15.4395), ("Linz", 48.3069, 14.2858)]},
]

# Générer les données des magasins
stores = []
store_id = 1
for country_info in eu_cities:
    country = country_info["country"]
    for city_info in country_info["cities"]:
        city, lat, lon = city_info
        num_stores = random.randint(1, 4)
        for _ in range(num_stores):
            if store_id > 100:
                break
            stores.append({
                "StoreID": store_id,
                "StoreName": f"Store {store_id}",
                "Country": country,
                "City": city,
                "Latitude": lat,
                "Longitude": lon
            })
            store_id += 1

# Générer les données des produits
products = [{"ProductID": i, "ProductName": f"Product {i}", "Category": random.choice(["Dairy", "Bakery", "Beverage"]), "ReplenishmentThreshold": random.randint(30, 100)} for i in range(1, 21)]

# Générer les données des stocks
inventory = [{"StoreID": random.randint(1, 100), "ProductID": random.randint(1, 20), "StockLevel": random.randint(0, 200)} for _ in range(500)]

# Générer les données des ventes
sales = []
start_date = datetime(2025, 1, 1)
for _ in range(1000):
    sales.append({
        "Date": start_date + timedelta(days=random.randint(0, 30)),
        "StoreID": random.randint(1, 100),
        "ProductID": random.randint(1, 20),
        "QuantitySold": random.randint(1, 20)
    })

# Générer les données des commandes de réapprovisionnement
replenishment_orders = []
for _ in range(500):
    replenishment_orders.append({
        "OrderID": _+1,
        "StoreID": random.randint(1, 100),
        "ProductID": random.randint(1, 20),
        "OrderStatus": random.choice(["Pending", "Delivered"]),
        "Quantity": random.randint(50, 200),
        "DeliveryDate": start_date + timedelta(days=random.randint(1, 30))
    })

# Sauvegarder les données en fichiers CSV
pd.DataFrame(stores).to_csv("Stores.csv", index=False)
pd.DataFrame(products).to_csv("Products.csv", index=False)
pd.DataFrame(inventory).to_csv("Inventory.csv", index=False)
pd.DataFrame(sales).to_csv("Sales.csv", index=False)
pd.DataFrame(replenishment_orders).to_csv("ReplenishmentOrders.csv", index=False)

print("Datasets generated and saved as CSV files.")

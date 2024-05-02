headers = {
    "Content-Type": "application/json",
   }

#Create a new user
user_body = {
    "firstName": "Ama",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

#Products_ids
product_ids = {
    "ids": [1, 2, 3]
}

#Crear kits
kit_body = {
    "name": "New kit",
    "card": {
        "id": 1,
        "name": "New kit"
    },
    "productsList":6,
    "id": 8,
    "productsCount": 0
   }

kit_body_empty={}
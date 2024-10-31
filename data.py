# data.py

sports_items = [
    {"id": "1", "name": "Sepeda Gunung", "description": "Sepeda gunung dengan suspensi penuh.", "price": 50000},
    {"id": "2", "name": "Perahu Kayak", "description": "Perahu kayak untuk dua orang.", "price": 150000},
    {"id": "3", "name": "Sepatu Hiking", "description": "Sepatu hiking yang nyaman untuk perjalanan jauh.", "price": 30000},
    {"id": "4", "name": "Tenda Camping", "description": "Tenda camping untuk empat orang.", "price": 120000},
    {"id": "5", "name": "Paddle Board", "description": "Paddle board untuk bersantai di atas air.", "price": 70000},
]

# Detail produk yang lebih lengkap
item_details = {item['id']: {**item, "customerReviews": []} for item in sports_items}

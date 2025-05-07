from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S22", "+79007654321"),
    Smartphone("Xiaomi", "Mi 11", "+79009876543"),
    Smartphone("Google", "Pixel 6", "+79005432123"),
    Smartphone("OnePlus", "9 Pro", "+79006789012")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
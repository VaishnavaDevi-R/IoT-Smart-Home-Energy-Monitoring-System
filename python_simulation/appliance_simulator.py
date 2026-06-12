from datetime import datetime

APPLIANCES = {
    "LED Bulb": 10,
    "Fan": 75,
    "Laptop": 65,
    "TV": 120,
    "Refrigerator": 180,
    "Washing Machine": 500,
    "Air Conditioner": 1500,
    "Water Heater": 2000
}


def get_active_appliances():

    hour = datetime.now().hour

    if 5 <= hour < 8:
        return [
            "LED Bulb",
            "Fan",
            "Water Heater"
        ]

    elif 8 <= hour < 12:
        return [
            "Fan",
            "Laptop",
            "Refrigerator"
        ]

    elif 12 <= hour < 17:
        return [
            "Fan",
            "Laptop",
            "Refrigerator"
        ]

    elif 17 <= hour < 22:
        return [
            "LED Bulb",
            "TV",
            "Fan",
            "Air Conditioner",
            "Refrigerator"
        ]

    else:
        return [
            "Air Conditioner",
            "Refrigerator"
        ]


def calculate_total_power():

    active_devices = get_active_appliances()

    total_power = sum(
        APPLIANCES[device]
        for device in active_devices
    )

    return active_devices, total_power
import random

def generate_sensor_data():

    voltage = round(random.uniform(220, 240), 2)

    current = round(random.uniform(0.5, 10.0), 2)

    return {
        "voltage": voltage,
        "current": current
    }
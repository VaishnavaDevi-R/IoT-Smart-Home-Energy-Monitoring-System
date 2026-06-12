from python_simulation.appliance_simulator import calculate_total_power

VOLTAGE = 230


def generate_sensor_data():

    active_devices, power = calculate_total_power()

    current = round(power / VOLTAGE, 2)

    return {
        "voltage": VOLTAGE,
        "current": current,
        "power": power,
        "active_devices": active_devices
    }
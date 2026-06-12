def calculate_energy_metrics(voltage, current):

    power = round(voltage * current, 2)

    hours = 1

    energy = round(power / 1000 * hours, 3)

    return {
        "power": power,
        "energy": energy
    }
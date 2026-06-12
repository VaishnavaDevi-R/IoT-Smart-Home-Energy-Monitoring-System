def calculate_energy_metrics(power):

    hours = 1

    energy = round(
        power / 1000 * hours,
        3
    )

    return {
        "power": power,
        "energy": energy
    }
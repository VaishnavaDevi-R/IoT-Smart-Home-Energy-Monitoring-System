def calculate_energy_metrics(power):

    HOURS = 1

    energy = round(
        (power / 1000) * HOURS,
        3
    )

    return {
        "power": power,
        "energy": energy
    }
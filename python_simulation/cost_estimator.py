TARIFF_PER_KWH = 8


def estimate_cost(energy):

    return round(
        energy * TARIFF_PER_KWH,
        2
    )
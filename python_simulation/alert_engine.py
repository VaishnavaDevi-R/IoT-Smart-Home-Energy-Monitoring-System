def generate_alert(power):

    if power >= 2000:
        return "HIGH_USAGE"

    elif power >= 1000:
        return "MEDIUM_USAGE"

    else:
        return "NORMAL"
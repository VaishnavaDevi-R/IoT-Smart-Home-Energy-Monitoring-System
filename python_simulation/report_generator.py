import csv
import os
from datetime import datetime

CSV_FILE = "data/energy_logs.csv"

def log_to_csv(sensor_data, metrics, cost):

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Voltage",
                "Current",
                "Power",
                "Energy",
                "Cost"
            ])

        writer.writerow([
            datetime.now(),
            sensor_data["voltage"],
            sensor_data["current"],
            metrics["power"],
            metrics["energy"],
            cost
        ])
from python_simulation.simulator import generate_sensor_data
from python_simulation.energy_calculator import calculate_energy_metrics
from python_simulation.cost_estimator import estimate_cost
from python_simulation.alert_engine import generate_alert
from python_simulation.report_generator import log_to_csv
from python_simulation.thingspeak_uploader import upload_to_thingspeak
from python_simulation.pdf_report_generator import generate_pdf_report

def main():

    sensor_data = generate_sensor_data()

    metrics = calculate_energy_metrics(
        sensor_data["power"]
    )

    cost = estimate_cost(
        metrics["energy"]
    )

    alert = generate_alert(
        metrics["power"]
    )

    log_to_csv(
        sensor_data,
        metrics,
        cost
    )

    upload_to_thingspeak(
        sensor_data["voltage"],
        sensor_data["current"],
        metrics["power"],
        metrics["energy"],
        cost,
        alert
    )

    generate_pdf_report(
        sensor_data["voltage"],
        sensor_data["current"],
        metrics["power"],
        metrics["energy"],
        cost,
        alert
    )

    print("\n==============================")
    print(" SMART HOME ENERGY MONITOR ")
    print("==============================")

    print("\nActive Appliances:")

    for appliance in sensor_data["active_devices"]:
        print(f"• {appliance}")

    print(f"\nVoltage : {sensor_data['voltage']} V")
    print(f"Current : {sensor_data['current']} A")
    print(f"Power   : {metrics['power']} W")
    print(f"Energy  : {metrics['energy']} kWh")
    print(f"Cost    : ₹{cost}")
    print(f"Alert   : {alert}")

    print("\n==============================\n")


if __name__ == "__main__":
    main()
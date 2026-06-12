from python_simulation.simulator import generate_sensor_data
from python_simulation.energy_calculator import calculate_energy_metrics
from python_simulation.cost_estimator import estimate_cost
from python_simulation.report_generator import log_to_csv

def main():

    sensor_data = generate_sensor_data()

    metrics = calculate_energy_metrics(
        sensor_data["voltage"],
        sensor_data["current"]
    )

    cost = estimate_cost(metrics["energy"])

    log_to_csv(
        sensor_data,
        metrics,
        cost
    )

    print("\n====== SMART HOME ENERGY MONITOR ======")
    print(f"Voltage : {sensor_data['voltage']} V")
    print(f"Current : {sensor_data['current']} A")
    print(f"Power   : {metrics['power']} W")
    print(f"Energy  : {metrics['energy']} kWh")
    print(f"Cost    : ₹{cost}")
    print("======================================")

if __name__ == "__main__":
    main()
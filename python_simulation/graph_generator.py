import os
import pandas as pd
import matplotlib.pyplot as plt

OUTPUT_DIR = "outputs/graphs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_graphs():

    # -----------------------------
    # Energy Logs Charts
    # -----------------------------

    energy_logs = "data/energy_logs.csv"

    if os.path.exists(energy_logs):

        df = pd.read_csv(energy_logs)

        # Power Chart
        plt.figure(figsize=(10, 5))
        plt.plot(df["Power"], marker="o")
        plt.title("Power Consumption Trend")
        plt.xlabel("Reading")
        plt.ylabel("Power (W)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/power_chart.png")
        plt.close()

        # Energy Chart
        plt.figure(figsize=(10, 5))
        plt.plot(df["Energy"], marker="o")
        plt.title("Energy Consumption Trend")
        plt.xlabel("Reading")
        plt.ylabel("Energy (kWh)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/energy_chart.png")
        plt.close()

        # Cost Chart
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(df)), df["Cost"])
        plt.title("Cost Analysis")
        plt.xlabel("Reading")
        plt.ylabel("Cost (₹)")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/cost_chart.png")
        plt.close()

    # -----------------------------
    # Daily Usage Chart
    # -----------------------------

    daily_file = "data/daily_usage.csv"

    if os.path.exists(daily_file):

        daily_df = pd.read_csv(daily_file)

        plt.figure(figsize=(10, 5))
        plt.bar(
            daily_df["Timestamp"].astype(str),
            daily_df["Energy"]
        )

        plt.title("Daily Energy Consumption")
        plt.xlabel("Date")
        plt.ylabel("Energy (kWh)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(
            f"{OUTPUT_DIR}/daily_usage_chart.png"
        )

        plt.close()

    # -----------------------------
    # Monthly Usage Chart
    # -----------------------------

    monthly_file = "data/monthly_usage.csv"

    if os.path.exists(monthly_file):

        monthly_df = pd.read_csv(monthly_file)

        plt.figure(figsize=(10, 5))
        plt.bar(
            monthly_df["Timestamp"].astype(str),
            monthly_df["Energy"]
        )

        plt.title("Monthly Energy Consumption")
        plt.xlabel("Month")
        plt.ylabel("Energy (kWh)")
        plt.tight_layout()

        plt.savefig(
            f"{OUTPUT_DIR}/monthly_usage_chart.png"
        )

        plt.close()

    print("✅ All Graphs Generated Successfully")
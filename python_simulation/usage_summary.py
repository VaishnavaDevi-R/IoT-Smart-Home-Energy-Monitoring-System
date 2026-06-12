import pandas as pd
import os


def generate_usage_summaries():

    source_file = "data/energy_logs.csv"

    if not os.path.exists(source_file):
        print("❌ energy_logs.csv not found")
        return

    df = pd.read_csv(source_file)

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # Daily Summary
    daily = (
        df.groupby(df["Timestamp"].dt.date)
        .agg({
            "Energy": "sum",
            "Cost": "sum",
            "Power": "mean"
        })
        .reset_index()
    )

    daily.to_csv(
        "data/daily_usage.csv",
        index=False
    )

    # Monthly Summary
    monthly = (
        df.groupby(df["Timestamp"].dt.to_period("M"))
        .agg({
            "Energy": "sum",
            "Cost": "sum",
            "Power": "mean"
        })
        .reset_index()
    )

    monthly.to_csv(
        "data/monthly_usage.csv",
        index=False
    )

    print("✅ Daily Summary Generated")
    print("✅ Monthly Summary Generated")
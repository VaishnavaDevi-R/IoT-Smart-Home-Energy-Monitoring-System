import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Smart Home Energy Monitor",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Smart Home Energy Monitoring System")

csv_file = "data/energy_logs.csv"

if os.path.exists(csv_file):

    df = pd.read_csv(csv_file)

    latest = df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Voltage",
            f"{latest['Voltage']} V"
        )

    with col2:
        st.metric(
            "Current",
            f"{latest['Current']} A"
        )

    with col3:
        st.metric(
            "Power",
            f"{latest['Power']} W"
        )

    with col4:
        st.metric(
            "Cost",
            f"₹{latest['Cost']}"
        )
        st.subheader("🏠 Active Appliances")

        st.write(
            latest["ActiveDevices"]
        )

    st.divider()

    st.subheader("📈 Power Consumption Trend")

    fig1 = px.line(
        df,
        y="Power",
        title="Power Usage"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("⚡ Energy Consumption")

    fig2 = px.line(
        df,
        y="Energy",
        title="Energy Consumption"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("💰 Cost Analysis")

    fig3 = px.bar(
        df,
        y="Cost",
        title="Estimated Cost"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader("📄 Recent Records")

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )

else:

    st.warning(
        "No energy logs found. Run main.py first."
    )
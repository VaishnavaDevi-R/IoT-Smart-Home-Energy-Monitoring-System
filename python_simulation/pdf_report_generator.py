from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_pdf_report(
    voltage,
    current,
    power,
    energy,
    cost,
    alert
):

    pdf_file = "outputs/energy_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Smart Home Energy Monitoring Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))

    report_time = Paragraph(
        f"Generated: {datetime.now()}",
        styles["Normal"]
    )

    content.append(report_time)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Voltage: {voltage} V",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Current: {current} A",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Power: {power} W",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Energy: {energy} kWh",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Estimated Cost: ₹{cost}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Alert Status: {alert}",
            styles["Normal"]
        )
    )

    doc.build(content)

    print("✅ PDF Report Generated")
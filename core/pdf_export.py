from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def _money(value):
    return f"PKR {value:,.0f}"


def build_pdf(profile, results, appliances, roof, pricing):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=28, leftMargin=28, topMargin=28, bottomMargin=28)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Pakistan Solar Panel Requirement System", styles["Title"]))
    story.append(Paragraph("Customer Quotation / Proposal", styles["Heading2"]))
    story.append(Spacer(1, 12))

    customer_data = [
        ["Customer", profile.get("name", "-")],
        ["Phone", profile.get("phone", "-")],
        ["City", profile.get("city", "-")],
        ["Utility", profile.get("utility", "-")],
        ["System Type", profile.get("system_type", "-")],
        ["Monthly Bill", _money(profile.get("monthly_bill_pkr", 0))],
        ["Monthly Units", f"{profile.get('monthly_units_kwh', 0)} kWh"],
    ]
    t1 = Table(customer_data, colWidths=[150, 350])
    t1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e0f2fe")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ]))
    story.append(t1)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Recommended System", styles["Heading2"]))
    rec_data = [
        ["Solar Size", f"{results.get('solar_size_kw', 0):.2f} kW"],
        ["Inverter", f"{results.get('inverter_kw', 0):.2f} kW"],
        ["Battery", f"{results.get('battery_kwh', 0):.2f} kWh ({results.get('battery_type', '-')})"],
        ["Monthly Generation", f"{results.get('monthly_generation', 0):,.0f} kWh"],
        ["Monthly Savings", _money(results.get('monthly_savings', 0))],
        ["Payback", f"{results.get('payback_years', 0):.1f} years"],
        ["Roof Capacity", f"{results.get('roof_capacity_kw', 0):.2f} kW"],
    ]
    t2 = Table(rec_data, colWidths=[150, 350])
    t2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dcfce7")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    story.append(t2)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Cost Breakdown", styles["Heading2"]))
    cost_data = [
        ["Panels", _money(results.get("panel_cost", 0))],
        ["Inverter", _money(results.get("inverter_cost", 0))],
        ["Battery", _money(results.get("battery_cost", 0))],
        ["Structure", _money(results.get("structure_cost", 0))],
        ["BOS", _money(results.get("bos_cost", 0))],
        ["Labor", _money(results.get("labor_cost", 0))],
        ["Transport", _money(results.get("transport_cost", 0))],
        ["Documentation", _money(results.get("documentation_cost", 0))],
        ["Contingency", _money(results.get("contingency", 0))],
        ["Total", _money(results.get("total_cost", 0))],
    ]
    t3 = Table(cost_data, colWidths=[150, 350])
    t3.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("BACKGROUND", (0, 9), (-1, 9), colors.HexColor("#fde68a")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    story.append(t3)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Selected Appliances", styles["Heading2"]))
    appliance_rows = [["Name", "Watts", "Qty", "Hours", "On Solar", "Backup"]]
    for item in appliances:
        appliance_rows.append([
            item.get("name", "-"),
            str(item.get("watts", 0)),
            str(item.get("qty", 0)),
            str(item.get("hours", 0)),
            "Yes" if item.get("on_solar", False) else "No",
            "Yes" if item.get("backup", False) else "No",
        ])
    t4 = Table(appliance_rows, repeatRows=1)
    t4.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbeafe")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
    ]))
    story.append(t4)
    story.append(Spacer(1, 14))

    if results.get("warnings"):
        story.append(Paragraph("Warnings / Notes", styles["Heading2"]))
        for w in results["warnings"]:
            story.append(Paragraph(f"• {w}", styles["BodyText"]))
        story.append(Spacer(1, 8))

    story.append(Paragraph("This quotation is an estimate for planning purposes. Final site survey, utility rules, and market prices may change the final offer.", styles["Italic"]))
    doc.build(story)
    buffer.seek(0)
    return buffer
